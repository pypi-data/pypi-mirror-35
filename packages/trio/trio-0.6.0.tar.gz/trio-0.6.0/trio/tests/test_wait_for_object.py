import os
import time

import pytest

on_windows = (os.name == "nt")
# Mark all the tests in this file as being windows-only
pytestmark = pytest.mark.skipif(not on_windows, reason="windows only")

from .._core.tests.tutil import slow
from .. import _core
from .. import _timeouts
if on_windows:
    from .._core._windows_cffi import ffi, kernel32
    from .._wait_for_object import WaitForSingleObject, WaitForMultipleObjects_sync, run_sync_in_worker_thread


async def test_WaitForMultipleObjects_sync():
    # This does a series of tests where we set/close the handle before
    # initiating the waiting for it.
    #
    # Note that closing the handle (not signaling) will cause the
    # *initiation* of a wait to return immediately. But closing a handle
    # that is already being waited on will not stop whatever is waiting
    # for it.

    # One handle
    handle1 = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    kernel32.SetEvent(handle1)
    WaitForMultipleObjects_sync(handle1)
    kernel32.CloseHandle(handle1)
    print('test_WaitForMultipleObjects_sync one OK')

    # Two handles, signal first
    handle1 = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    handle2 = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    kernel32.SetEvent(handle1)
    WaitForMultipleObjects_sync(handle1, handle2)
    kernel32.CloseHandle(handle1)
    kernel32.CloseHandle(handle2)
    print('test_WaitForMultipleObjects_sync set first OK')

    # Two handles, signal second
    handle1 = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    handle2 = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    kernel32.SetEvent(handle2)
    WaitForMultipleObjects_sync(handle1, handle2)
    kernel32.CloseHandle(handle1)
    kernel32.CloseHandle(handle2)
    print('test_WaitForMultipleObjects_sync set second OK')

    # Two handles, close first
    handle1 = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    handle2 = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    kernel32.CloseHandle(handle1)
    with pytest.raises(OSError):
        WaitForMultipleObjects_sync(handle1, handle2)
    kernel32.CloseHandle(handle2)
    print('test_WaitForMultipleObjects_sync close first OK')

    # Two handles, close second
    handle1 = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    handle2 = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    kernel32.CloseHandle(handle2)
    with pytest.raises(OSError):
        WaitForMultipleObjects_sync(handle1, handle2)
    kernel32.CloseHandle(handle1)
    print('test_WaitForMultipleObjects_sync close second OK')


@slow
async def test_WaitForMultipleObjects_sync_slow():
    # This does a series of test in which the main thread sync-waits for
    # handles, while we spawn a thread to set the handles after a short while.

    TIMEOUT = 0.3

    # One handle
    handle1 = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    t0 = _core.current_time()
    async with _core.open_nursery() as nursery:
        nursery.start_soon(
            run_sync_in_worker_thread, WaitForMultipleObjects_sync, handle1
        )
        await _timeouts.sleep(TIMEOUT)
        # If we would comment the line below, the above thread will be stuck,
        # and trio wont exit this scope
        kernel32.SetEvent(handle1)
    t1 = _core.current_time()
    assert TIMEOUT <= (t1 - t0) < 2.0 * TIMEOUT
    kernel32.CloseHandle(handle1)
    print('test_WaitForMultipleObjects_sync_slow one OK')

    # Two handles, signal first
    handle1 = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    handle2 = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    t0 = _core.current_time()
    async with _core.open_nursery() as nursery:
        nursery.start_soon(
            run_sync_in_worker_thread, WaitForMultipleObjects_sync, handle1,
            handle2
        )
        await _timeouts.sleep(TIMEOUT)
        kernel32.SetEvent(handle1)
    t1 = _core.current_time()
    assert TIMEOUT <= (t1 - t0) < 2.0 * TIMEOUT
    kernel32.CloseHandle(handle1)
    kernel32.CloseHandle(handle2)
    print('test_WaitForMultipleObjects_sync_slow thread-set first OK')

    # Two handles, signal second
    handle1 = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    handle2 = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    t0 = _core.current_time()
    async with _core.open_nursery() as nursery:
        nursery.start_soon(
            run_sync_in_worker_thread, WaitForMultipleObjects_sync, handle1,
            handle2
        )
        await _timeouts.sleep(TIMEOUT)
        kernel32.SetEvent(handle2)
    t1 = _core.current_time()
    assert TIMEOUT <= (t1 - t0) < 2.0 * TIMEOUT
    kernel32.CloseHandle(handle1)
    kernel32.CloseHandle(handle2)
    print('test_WaitForMultipleObjects_sync_slow thread-set second OK')


async def test_WaitForSingleObject():
    # This does a series of test for setting/closing the handle before
    # initiating the wait.

    # Test already set
    handle = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    kernel32.SetEvent(handle)
    await WaitForSingleObject(handle)  # should return at once
    kernel32.CloseHandle(handle)
    print('test_WaitForSingleObject already set OK')

    # Test already set, as int
    handle = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    handle_int = int(ffi.cast("intptr_t", handle))
    kernel32.SetEvent(handle)
    await WaitForSingleObject(handle_int)  # should return at once
    kernel32.CloseHandle(handle)
    print('test_WaitForSingleObject already set OK')

    # Test already closed
    handle = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    kernel32.CloseHandle(handle)
    with pytest.raises(OSError):
        await WaitForSingleObject(handle)  # should return at once
    print('test_WaitForSingleObject already closed OK')

    # Not a handle
    with pytest.raises(TypeError):
        await WaitForSingleObject("not a handle")  # Wrong type
    # with pytest.raises(OSError):
    #     await WaitForSingleObject(99)  # If you're unlucky, it actually IS a handle :(
    print('test_WaitForSingleObject not a handle OK')


@slow
async def test_WaitForSingleObject_slow():
    # This does a series of test for setting the handle in another task,
    # and cancelling the wait task.

    # Set the timeout used in the tests. We test the waiting time against
    # the timeout with a certain margin.
    TIMEOUT = 0.3

    async def signal_soon_async(handle):
        await _timeouts.sleep(TIMEOUT)
        kernel32.SetEvent(handle)

    # Test handle is SET after TIMEOUT in separate coroutine

    handle = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    t0 = _core.current_time()

    async with _core.open_nursery() as nursery:
        nursery.start_soon(WaitForSingleObject, handle)
        nursery.start_soon(signal_soon_async, handle)

    kernel32.CloseHandle(handle)
    t1 = _core.current_time()
    assert TIMEOUT <= (t1 - t0) < 2.0 * TIMEOUT
    print('test_WaitForSingleObject_slow set from task OK')

    # Test handle is SET after TIMEOUT in separate coroutine, as int

    handle = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    handle_int = int(ffi.cast("intptr_t", handle))
    t0 = _core.current_time()

    async with _core.open_nursery() as nursery:
        nursery.start_soon(WaitForSingleObject, handle_int)
        nursery.start_soon(signal_soon_async, handle)

    kernel32.CloseHandle(handle)
    t1 = _core.current_time()
    assert TIMEOUT <= (t1 - t0) < 2.0 * TIMEOUT
    print('test_WaitForSingleObject_slow set from task as int OK')

    # Test handle is CLOSED after 1 sec - NOPE see comment above

    pass

    # Test cancellation

    handle = kernel32.CreateEventA(ffi.NULL, True, False, ffi.NULL)
    t0 = _core.current_time()

    with _timeouts.move_on_after(TIMEOUT):
        await WaitForSingleObject(handle)

    kernel32.CloseHandle(handle)
    t1 = _core.current_time()
    assert TIMEOUT <= (t1 - t0) < 2.0 * TIMEOUT
    print('test_WaitForSingleObject_slow cancellation OK')
