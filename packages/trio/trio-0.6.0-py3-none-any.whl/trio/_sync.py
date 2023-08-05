import operator
from collections import deque, OrderedDict

import attr
import outcome

from . import _core
from ._util import aiter_compat

__all__ = [
    "Event",
    "CapacityLimiter",
    "Semaphore",
    "Lock",
    "StrictFIFOLock",
    "Condition",
    "Queue",
]


@attr.s(repr=False, cmp=False, hash=False)
class Event:
    """A waitable boolean value useful for inter-task synchronization,
    inspired by :class:`threading.Event`.

    An event object manages an internal boolean flag, which is initially
    False, and tasks can wait for it to become True.

    """

    _lot = attr.ib(default=attr.Factory(_core.ParkingLot), init=False)
    _flag = attr.ib(default=False, init=False)

    def is_set(self):
        """Return the current value of the internal flag.

        """
        return self._flag

    @_core.enable_ki_protection
    def set(self):
        """Set the internal flag value to True, and wake any waiting tasks.

        """
        self._flag = True
        self._lot.unpark_all()

    def clear(self):
        """Set the internal flag value to False.

        """
        self._flag = False

    async def wait(self):
        """Block until the internal flag value becomes True.

        If it's already True, then this method is still a checkpoint, but
        otherwise returns immediately.

        """
        if self._flag:
            await _core.checkpoint()
        else:
            await self._lot.park()

    def statistics(self):
        """Return an object containing debugging information.

        Currently the following fields are defined:

        * ``tasks_waiting``: The number of tasks blocked on this event's
          :meth:`wait` method.

        """
        return self._lot.statistics()


def async_cm(cls):
    @_core.enable_ki_protection
    async def __aenter__(self):
        await self.acquire()

    __aenter__.__qualname__ = cls.__qualname__ + ".__aenter__"
    cls.__aenter__ = __aenter__

    @_core.enable_ki_protection
    async def __aexit__(self, *args):
        self.release()

    __aexit__.__qualname__ = cls.__qualname__ + ".__aexit__"
    cls.__aexit__ = __aexit__
    return cls


@attr.s(frozen=True)
class _CapacityLimiterStatistics:
    borrowed_tokens = attr.ib()
    total_tokens = attr.ib()
    borrowers = attr.ib()
    tasks_waiting = attr.ib()


@async_cm
class CapacityLimiter:
    """An object for controlling access to a resource with limited capacity.

    Sometimes you need to put a limit on how many tasks can do something at
    the same time. For example, you might want to use some threads to run
    multiple blocking I/O operations in parallel... but if you use too many
    threads at once, then your system can become overloaded and it'll actually
    make things slower. One popular solution is to impose a policy like "run
    up to 40 threads at the same time, but no more". But how do you implement
    a policy like this?

    That's what :class:`CapacityLimiter` is for. You can think of a
    :class:`CapacityLimiter` object as a sack that starts out holding some fixed
    number of tokens::

       limit = trio.CapacityLimiter(40)

    Then tasks can come along and borrow a token out of the sack::

       # Borrow a token:
       async with limit:
           # We are holding a token!
           await perform_expensive_operation()
       # Exiting the 'async with' block puts the token back into the sack

    And crucially, if you try to borrow a token but the sack is empty, then
    you have to wait for another task to finish what it's doing and put its
    token back first before you can take it and continue.

    Another way to think of it: a :class:`CapacityLimiter` is like a sofa with a
    fixed number of seats, and if they're all taken then you have to wait for
    someone to get up before you can sit down.

    By default, :func:`run_sync_in_worker_thread` uses a
    :class:`CapacityLimiter` to limit the number of threads running at once;
    see :func:`current_default_worker_thread_limiter` for details.

    If you're familiar with semaphores, then you can think of this as a
    restricted semaphore that's specialized for one common use case, with
    additional error checking. For a more traditional semaphore, see
    :class:`Semaphore`.

    .. note::

       Don't confuse this with the `"leaky bucket"
       <https://en.wikipedia.org/wiki/Leaky_bucket>`__ or `"token bucket"
       <https://en.wikipedia.org/wiki/Token_bucket>`__ algorithms used to
       limit bandwidth usage on networks. The basic idea of using tokens to
       track a resource limit is similar, but this is a very simple sack where
       tokens aren't automatically created or destroyed over time; they're
       just borrowed and then put back.

    """

    def __init__(self, total_tokens):
        self._lot = _core.ParkingLot()
        self._borrowers = set()
        # Maps tasks attempting to acquire -> borrower, to handle on-behalf-of
        self._pending_borrowers = {}
        # invoke the property setter for validation
        self.total_tokens = total_tokens
        assert self._total_tokens == total_tokens

    def __repr__(self):
        return (
            "<trio.CapacityLimiter at {:#x}, {}/{} with {} waiting>".format(
                id(self), len(self._borrowers), self._total_tokens,
                len(self._lot)
            )
        )

    @property
    def total_tokens(self):
        """The total capacity available.

        You can change :attr:`total_tokens` by assigning to this attribute. If
        you make it larger, then the appropriate number of waiting tasks will
        be woken immediately to take the new tokens. If you decrease
        total_tokens below the number of tasks that are currently using the
        resource, then all current tasks will be allowed to finish as normal,
        but no new tasks will be allowed in until the total number of tasks
        drops below the new total_tokens.

        """
        return self._total_tokens

    def _wake_waiters(self):
        available = self._total_tokens - len(self._borrowers)
        for woken in self._lot.unpark(count=available):
            self._borrowers.add(self._pending_borrowers.pop(woken))

    @total_tokens.setter
    def total_tokens(self, new_total_tokens):
        if not isinstance(new_total_tokens, int):
            raise TypeError("total_tokens must be an int")
        if new_total_tokens < 1:
            raise ValueError("total_tokens must be >= 1")
        self._total_tokens = new_total_tokens
        self._wake_waiters()

    @property
    def borrowed_tokens(self):
        """The amount of capacity that's currently in use.

        """
        return len(self._borrowers)

    @property
    def available_tokens(self):
        """The amount of capacity that's available to use.

        """
        return self.total_tokens - self.borrowed_tokens

    @_core.enable_ki_protection
    def acquire_nowait(self):
        """Borrow a token from the sack, without blocking.

        Raises:
          WouldBlock: if no tokens are available.
          RuntimeError: if the current task already holds one of this sack's
              tokens.

        """
        self.acquire_on_behalf_of_nowait(_core.current_task())

    @_core.enable_ki_protection
    def acquire_on_behalf_of_nowait(self, borrower):
        """Borrow a token from the sack on behalf of ``borrower``, without
        blocking.

        Args:
          borrower: A :class:`trio.hazmat.Task` or arbitrary opaque object
             used to record who is borrowing this token. This is used by
             :func:`run_sync_in_worker_thread` to allow threads to "hold
             tokens", with the intention in the future of using it to `allow
             deadlock detection and other useful things
             <https://github.com/python-trio/trio/issues/182>`__

        Raises:
          WouldBlock: if no tokens are available.
          RuntimeError: if ``borrower`` already holds one of this sack's
              tokens.

        """
        if borrower in self._borrowers:
            raise RuntimeError(
                "this borrower is already holding one of this "
                "CapacityLimiter's tokens"
            )
        if len(self._borrowers) < self._total_tokens and not self._lot:
            self._borrowers.add(borrower)
        else:
            raise _core.WouldBlock

    @_core.enable_ki_protection
    async def acquire(self):
        """Borrow a token from the sack, blocking if necessary.

        Raises:
          RuntimeError: if the current task already holds one of this sack's
              tokens.

        """
        await self.acquire_on_behalf_of(_core.current_task())

    @_core.enable_ki_protection
    async def acquire_on_behalf_of(self, borrower):
        """Borrow a token from the sack on behalf of ``borrower``, blocking if
        necessary.

        Args:
          borrower: A :class:`trio.hazmat.Task` or arbitrary opaque object
             used to record who is borrowing this token; see
             :meth:`acquire_on_behalf_of_nowait` for details.

        Raises:
          RuntimeError: if ``borrower`` task already holds one of this sack's
             tokens.

        """
        await _core.checkpoint_if_cancelled()
        try:
            self.acquire_on_behalf_of_nowait(borrower)
        except _core.WouldBlock:
            task = _core.current_task()
            self._pending_borrowers[task] = borrower
            try:
                await self._lot.park()
            except _core.Cancelled:
                self._pending_borrowers.pop(task)
                raise
        except:
            await _core.cancel_shielded_checkpoint()
            raise
        else:
            await _core.cancel_shielded_checkpoint()

    @_core.enable_ki_protection
    def release(self):
        """Put a token back into the sack.

        Raises:
          RuntimeError: if the current task has not acquired one of this
              sack's tokens.

        """
        self.release_on_behalf_of(_core.current_task())

    @_core.enable_ki_protection
    def release_on_behalf_of(self, borrower):
        """Put a token back into the sack on behalf of ``borrower``.

        Raises:
          RuntimeError: if the given borrower has not acquired one of this
              sack's tokens.

        """
        if borrower not in self._borrowers:
            raise RuntimeError(
                "this borrower isn't holding any of this CapacityLimiter's "
                "tokens"
            )
        self._borrowers.remove(borrower)
        self._wake_waiters()

    def statistics(self):
        """Return an object containing debugging information.

        Currently the following fields are defined:

        * ``borrowed_tokens``: The number of tokens currently borrowed from
          the sack.
        * ``total_tokens``: The total number of tokens in the sack. Usually
          this will be larger than ``borrowed_tokens``, but it's possibly for
          it to be smaller if :attr:`total_tokens` was recently decreased.
        * ``borrowers``: A list of all tasks or other entities that currently
          hold a token.
        * ``tasks_waiting``: The number of tasks blocked on this
          :class:`CapacityLimiter`\'s :meth:`acquire` or
          :meth:`acquire_on_behalf_of` methods.

        """
        return _CapacityLimiterStatistics(
            borrowed_tokens=len(self._borrowers),
            total_tokens=self._total_tokens,
            # Use a list instead of a frozenset just in case we start to allow
            # one borrower to hold multiple tokens in the future
            borrowers=list(self._borrowers),
            tasks_waiting=len(self._lot),
        )


@async_cm
class Semaphore:
    """A `semaphore <https://en.wikipedia.org/wiki/Semaphore_(programming)>`__.

    A semaphore holds an integer value, which can be incremented by
    calling :meth:`release` and decremented by calling :meth:`acquire` – but
    the value is never allowed to drop below zero. If the value is zero, then
    :meth:`acquire` will block until someone calls :meth:`release`.

    If you're looking for a :class:`Semaphore` to limit the number of tasks
    that can access some resource simultaneously, then consider using a
    :class:`CapacityLimiter` instead.

    This object's interface is similar to, but different from, that of
    :class:`threading.Semaphore`.

    A :class:`Semaphore` object can be used as an async context manager; it
    blocks on entry but not on exit.

    Args:
      initial_value (int): A non-negative integer giving semaphore's initial
        value.
      max_value (int or None): If given, makes this a "bounded" semaphore that
        raises an error if the value is about to exceed the given
        ``max_value``.

    """

    def __init__(self, initial_value, *, max_value=None):
        if not isinstance(initial_value, int):
            raise TypeError("initial_value must be an int")
        if initial_value < 0:
            raise ValueError("initial value must be >= 0")
        if max_value is not None:
            if not isinstance(max_value, int):
                raise TypeError("max_value must be None or an int")
            if max_value < initial_value:
                raise ValueError("max_values must be >= initial_value")

        # Invariants:
        # bool(self._lot) implies self._value == 0
        # (or equivalently: self._value > 0 implies not self._lot)
        self._lot = _core.ParkingLot()
        self._value = initial_value
        self._max_value = max_value

    def __repr__(self):
        if self._max_value is None:
            max_value_str = ""
        else:
            max_value_str = ", max_value={}".format(self._max_value)
        return (
            "<trio.Semaphore({}{}) at {:#x}>"
            .format(self._value, max_value_str, id(self))
        )

    @property
    def value(self):
        """The current value of the semaphore.

        """
        return self._value

    @property
    def max_value(self):
        """The maximum allowed value. May be None to indicate no limit.

        """
        return self._max_value

    @_core.enable_ki_protection
    def acquire_nowait(self):
        """Attempt to decrement the semaphore value, without blocking.

        Raises:
          WouldBlock: if the value is zero.

        """
        if self._value > 0:
            assert not self._lot
            self._value -= 1
        else:
            raise _core.WouldBlock

    @_core.enable_ki_protection
    async def acquire(self):
        """Decrement the semaphore value, blocking if necessary to avoid
        letting it drop below zero.

        """
        await _core.checkpoint_if_cancelled()
        try:
            self.acquire_nowait()
        except _core.WouldBlock:
            await self._lot.park()
        else:
            await _core.cancel_shielded_checkpoint()

    @_core.enable_ki_protection
    def release(self):
        """Increment the semaphore value, possibly waking a task blocked in
        :meth:`acquire`.

        Raises:
          ValueError: if incrementing the value would cause it to exceed
              :attr:`max_value`.

        """
        if self._lot:
            assert self._value == 0
            self._lot.unpark(count=1)
        else:
            if self._max_value is not None and self._value == self._max_value:
                raise ValueError("semaphore released too many times")
            self._value += 1

    def statistics(self):
        """Return an object containing debugging information.

        Currently the following fields are defined:

        * ``tasks_waiting``: The number of tasks blocked on this semaphore's
          :meth:`acquire` method.

        """
        return self._lot.statistics()


@attr.s(frozen=True)
class _LockStatistics:
    locked = attr.ib()
    owner = attr.ib()
    tasks_waiting = attr.ib()


@async_cm
@attr.s(cmp=False, hash=False, repr=False)
class Lock:
    """A classic `mutex
    <https://en.wikipedia.org/wiki/Lock_(computer_science)>`__.

    This is a non-reentrant, single-owner lock. Unlike
    :class:`threading.Lock`, only the owner of the lock is allowed to release
    it.

    A :class:`Lock` object can be used as an async context manager; it
    blocks on entry but not on exit.

    """

    _lot = attr.ib(default=attr.Factory(_core.ParkingLot), init=False)
    _owner = attr.ib(default=None, init=False)

    def __repr__(self):
        if self.locked():
            s1 = "locked"
            s2 = " with {} waiters".format(len(self._lot))
        else:
            s1 = "unlocked"
            s2 = ""
        return (
            "<{} {} object at {:#x}{}>"
            .format(s1, self.__class__.__name__, id(self), s2)
        )

    def locked(self):
        """Check whether the lock is currently held.

        Returns:
          bool: True if the lock is held, False otherwise.

        """
        return self._owner is not None

    @_core.enable_ki_protection
    def acquire_nowait(self):
        """Attempt to acquire the lock, without blocking.

        Raises:
          WouldBlock: if the lock is held.

        """

        task = _core.current_task()
        if self._owner is task:
            raise RuntimeError("attempt to re-acquire an already held Lock")
        elif self._owner is None and not self._lot:
            # No-one owns it
            self._owner = task
        else:
            raise _core.WouldBlock

    @_core.enable_ki_protection
    async def acquire(self):
        """Acquire the lock, blocking if necessary.

        """
        await _core.checkpoint_if_cancelled()
        try:
            self.acquire_nowait()
        except _core.WouldBlock:
            # NOTE: it's important that the contended acquire path is just
            # "_lot.park()", because that's how Condition.wait() acquires the
            # lock as well.
            await self._lot.park()
        else:
            await _core.cancel_shielded_checkpoint()

    @_core.enable_ki_protection
    def release(self):
        """Release the lock.

        Raises:
          RuntimeError: if the calling task does not hold the lock.

        """
        task = _core.current_task()
        if task is not self._owner:
            raise RuntimeError("can't release a Lock you don't own")
        if self._lot:
            (self._owner,) = self._lot.unpark(count=1)
        else:
            self._owner = None

    def statistics(self):
        """Return an object containing debugging information.

        Currently the following fields are defined:

        * ``locked``: boolean indicating whether the lock is held.
        * ``owner``: the :class:`trio.hazmat.Task` currently holding the lock,
          or None if the lock is not held.
        * ``tasks_waiting``: The number of tasks blocked on this lock's
          :meth:`acquire` method.

        """
        return _LockStatistics(
            locked=self.locked(),
            owner=self._owner,
            tasks_waiting=len(self._lot),
        )


class StrictFIFOLock(Lock):
    """A variant of :class:`Lock` where tasks are guaranteed to acquire the
    lock in strict first-come-first-served order.

    An example of when this is useful is if you're implementing something like
    :class:`trio.ssl.SSLStream` or an HTTP/2 server using `h2
    <https://hyper-h2.readthedocs.io/>`__, where you have multiple concurrent
    tasks that are interacting with a shared state machine, and at
    unpredictable moments the state machine requests that a chunk of data be
    sent over the network. (For example, when using h2 simply reading incoming
    data can occasionally `create outgoing data to send
    <https://http2.github.io/http2-spec/#PING>`__.) The challenge is to make
    sure that these chunks are sent in the correct order, without being
    garbled.

    One option would be to use a regular :class:`Lock`, and wrap it around
    every interaction with the state machine::

        # This approach is sometimes workable but often sub-optimal; see below
        async with lock:
            state_machine.do_something()
            if state_machine.has_data_to_send():
                await conn.sendall(state_machine.get_data_to_send())

    But this can be problematic. If you're using h2 then *usually* reading
    incoming data doesn't create the need to send any data, so we don't want
    to force every task that tries to read from the network to sit and wait
    a potentially long time for ``sendall`` to finish. And in some situations
    this could even potentially cause a deadlock, if the remote peer is
    waiting for you to read some data before it accepts the data you're
    sending.

    :class:`StrictFIFOLock` provides an alternative. We can rewrite our
    example like::

        # Note: no awaits between when we start using the state machine and
        # when we block to take the lock!
        state_machine.do_something()
        if state_machine.has_data_to_send():
            # Notice that we fetch the data to send out of the state machine
            # *before* sleeping, so that other tasks won't see it.
            chunk = state_machine.get_data_to_send()
            async with strict_fifo_lock:
                await conn.sendall(chunk)

    First we do all our interaction with the state machine in a single
    scheduling quantum (notice there are no ``await``\s in there), so it's
    automatically atomic with respect to other tasks. And then if and only if
    we have data to send, we get in line to send it – and
    :class:`StrictFIFOLock` guarantees that each task will send its data in
    the same order that the state machine generated it.

    Currently, :class:`StrictFIFOLock` is simply an alias for :class:`Lock`,
    but (a) this may not always be true in the future, especially if trio ever
    implements `more sophisticated scheduling policies
    <https://github.com/python-trio/trio/issues/32>`__, and (b) the above code
    is relying on a pretty subtle property of its lock. Using a
    :class:`StrictFIFOLock` acts as an executable reminder that you're relying
    on this property.

    """


@attr.s(frozen=True)
class _ConditionStatistics:
    tasks_waiting = attr.ib()
    lock_statistics = attr.ib()


@async_cm
class Condition:
    """A classic `condition variable
    <https://en.wikipedia.org/wiki/Monitor_(synchronization)>`__, similar to
    :class:`threading.Condition`.

    A :class:`Condition` object can be used as an async context manager to
    acquire the underlying lock; it blocks on entry but not on exit.

    Args:
      lock (Lock): the lock object to use. If given, must be a
          :class:`trio.Lock`. If None, a new :class:`Lock` will be allocated
          and used.

    """

    def __init__(self, lock=None):
        if lock is None:
            lock = Lock()
        if not type(lock) is Lock:
            raise TypeError("lock must be a trio.Lock")
        self._lock = lock
        self._lot = _core.ParkingLot()

    def locked(self):
        """Check whether the underlying lock is currently held.

        Returns:
          bool: True if the lock is held, False otherwise.

        """
        return self._lock.locked()

    def acquire_nowait(self):
        """Attempt to acquire the underlying lock, without blocking.

        Raises:
          WouldBlock: if the lock is currently held.

        """
        return self._lock.acquire_nowait()

    async def acquire(self):
        """Acquire the underlying lock, blocking if necessary.

        """
        await self._lock.acquire()

    def release(self):
        """Release the underlying lock.

        """
        self._lock.release()

    @_core.enable_ki_protection
    async def wait(self):
        """Wait for another thread to call :meth:`notify` or
        :meth:`notify_all`.

        When calling this method, you must hold the lock. It releases the lock
        while waiting, and then re-acquires it before waking up.

        There is a subtlety with how this method interacts with cancellation:
        when cancelled it will block to re-acquire the lock before raising
        :exc:`Cancelled`. This may cause cancellation to be less prompt than
        expected. The advantage is that it makes code like this work::

           async with condition:
               await condition.wait()

        If we didn't re-acquire the lock before waking up, and :meth:`wait`
        were cancelled here, then we'd crash in ``condition.__aexit__`` when
        we tried to release the lock we no longer held.

        Raises:
          RuntimeError: if the calling task does not hold the lock.

        """
        if _core.current_task() is not self._lock._owner:
            raise RuntimeError("must hold the lock to wait")
        self.release()
        # NOTE: we go to sleep on self._lot, but we'll wake up on
        # self._lock._lot. That's all that's required to acquire a Lock.
        try:
            await self._lot.park()
        except:
            with _core.open_cancel_scope(shield=True):
                await self.acquire()
            raise

    def notify(self, n=1):
        """Wake one or more tasks that are blocked in :meth:`wait`.

        Args:
          n (int): The number of tasks to wake.

        Raises:
          RuntimeError: if the calling task does not hold the lock.

        """
        if _core.current_task() is not self._lock._owner:
            raise RuntimeError("must hold the lock to notify")
        self._lot.repark(self._lock._lot, count=n)

    def notify_all(self):
        """Wake all tasks that are currently blocked in :meth:`wait`.

        Raises:
          RuntimeError: if the calling task does not hold the lock.

        """
        if _core.current_task() is not self._lock._owner:
            raise RuntimeError("must hold the lock to notify")
        self._lot.repark_all(self._lock._lot)

    def statistics(self):
        """Return an object containing debugging information.

        Currently the following fields are defined:

        * ``tasks_waiting``: The number of tasks blocked on this condition's
          :meth:`wait` method.
        * ``lock_statistics``: The result of calling the underlying
          :class:`Lock`\s  :meth:`~Lock.statistics` method.

        """
        return _ConditionStatistics(
            tasks_waiting=len(self._lot),
            lock_statistics=self._lock.statistics(),
        )


@attr.s(frozen=True)
class _QueueStats:
    qsize = attr.ib()
    capacity = attr.ib()
    tasks_waiting_put = attr.ib()
    tasks_waiting_get = attr.ib()


# Like queue.Queue, with the notable difference that the capacity argument is
# mandatory.
class Queue:
    """A bounded queue suitable for inter-task communication.

    This class is generally modelled after :class:`queue.Queue`, but with the
    major difference that it is always bounded.

    A :class:`Queue` object can be used as an asynchronous iterator that
    dequeues objects one at a time. That is, these two loops are equivalent::

       async for obj in queue:
           ...

       while True:
           obj = await queue.get()
           ...

    Args:
      capacity (int): The maximum number of items allowed in the queue before
          :meth:`put` blocks. Choosing a sensible value here is important to
          ensure that backpressure is communicated promptly and avoid
          unnecessary latency. If in doubt, use 0.

    """

    def __init__(self, capacity):
        if not isinstance(capacity, int):
            raise TypeError("capacity must be an integer")
        if capacity < 0:
            raise ValueError("capacity must be >= 0")
        self.capacity = operator.index(capacity)
        # {task: None} ordered set
        self._get_wait = OrderedDict()
        # {task: queued value}
        self._put_wait = OrderedDict()
        # invariants:
        # if len(self._data) < self.capacity, then self._put_wait is empty
        # if len(self._data) > 0, then self._get_wait is empty
        self._data = deque()

    def __repr__(self):
        return (
            "<Queue({}) at {:#x} holding {} items>"
            .format(self.capacity, id(self), len(self._data))
        )

    def qsize(self):
        """Returns the number of items currently in the queue.

        There is some subtlety to interpreting this method's return value: see
        `issue #63 <https://github.com/python-trio/trio/issues/63>`__.

        """
        return len(self._data)

    def full(self):
        """Returns True if the queue is at capacity, False otherwise.

        There is some subtlety to interpreting this method's return value: see
        `issue #63 <https://github.com/python-trio/trio/issues/63>`__.

        """
        return len(self._data) == self.capacity

    def empty(self):
        """Returns True if the queue is empty, False otherwise.

        There is some subtlety to interpreting this method's return value: see
        `issue #63 <https://github.com/python-trio/trio/issues/63>`__.

        """
        return not self._data

    @_core.enable_ki_protection
    def put_nowait(self, obj):
        """Attempt to put an object into the queue, without blocking.

        Args:
          obj (object): The object to enqueue.

        Raises:
          WouldBlock: if the queue is full.

        """
        if self._get_wait:
            assert not self._data
            task, _ = self._get_wait.popitem(last=False)
            _core.reschedule(task, outcome.Value(obj))
        elif len(self._data) < self.capacity:
            self._data.append(obj)
        else:
            raise _core.WouldBlock()

    @_core.enable_ki_protection
    async def put(self, obj):
        """Put an object into the queue, blocking if necessary.

        Args:
          obj (object): The object to enqueue.

        """
        await _core.checkpoint_if_cancelled()
        try:
            self.put_nowait(obj)
        except _core.WouldBlock:
            pass
        else:
            await _core.cancel_shielded_checkpoint()
            return

        task = _core.current_task()
        self._put_wait[task] = obj

        def abort_fn(_):
            del self._put_wait[task]
            return _core.Abort.SUCCEEDED

        await _core.wait_task_rescheduled(abort_fn)

    @_core.enable_ki_protection
    def get_nowait(self):
        """Attempt to get an object from the queue, without blocking.

        Returns:
          object: The dequeued object.

        Raises:
          WouldBlock: if the queue is empty.

        """
        if self._put_wait:
            task, value = self._put_wait.popitem(last=False)
            # No need to check max_size, b/c we'll pop an item off again right
            # below.
            self._data.append(value)
            _core.reschedule(task)
        if self._data:
            value = self._data.popleft()
            return value
        raise _core.WouldBlock()

    @_core.enable_ki_protection
    async def get(self):
        """Get an object from the queue, blocking if necessary.

        Returns:
          object: The dequeued object.

        """
        await _core.checkpoint_if_cancelled()
        try:
            value = self.get_nowait()
        except _core.WouldBlock:
            pass
        else:
            await _core.cancel_shielded_checkpoint()
            return value

        # Queue doesn't have anything, we must wait.
        task = _core.current_task()

        def abort_fn(_):
            self._get_wait.pop(task)
            return _core.Abort.SUCCEEDED

        self._get_wait[task] = None
        value = await _core.wait_task_rescheduled(abort_fn)
        return value

    @aiter_compat
    def __aiter__(self):
        return self

    async def __anext__(self):
        return await self.get()

    def statistics(self):
        """Returns an object containing debugging information.

        Currently the following fields are defined:

        * ``qsize``: The number of items currently in the queue.
        * ``capacity``: The maximum number of items the queue can hold.
        * ``tasks_waiting_put``: The number of tasks blocked on this queue's
          :meth:`put` method.
        * ``tasks_waiting_get``: The number of tasks blocked on this queue's
          :meth:`get` method.

        """
        return _QueueStats(
            qsize=len(self._data),
            capacity=self.capacity,
            tasks_waiting_put=len(self._put_wait),
            tasks_waiting_get=len(self._get_wait),
        )
