import pytest

from pathlib import Path
import threading
import socket as stdlib_socket
import ssl as stdlib_ssl
from contextlib import contextmanager
from functools import partial

from OpenSSL import SSL
import trustme
from async_generator import async_generator, yield_, asynccontextmanager

import trio
from .. import _core
from .._highlevel_socket import SocketStream, SocketListener
from .._highlevel_generic import BrokenStreamError, aclose_forcefully
from .._core import ClosedResourceError
from .._highlevel_open_tcp_stream import open_tcp_stream
from .. import ssl as tssl
from .. import socket as tsocket
from .._util import ConflictDetector

from .._core.tests.tutil import slow

from ..testing import (
    assert_checkpoints,
    Sequencer,
    memory_stream_pair,
    lockstep_stream_pair,
    check_two_way_stream,
)

# We have two different kinds of echo server fixtures we use for testing. The
# first is a real server written using the stdlib ssl module and blocking
# sockets. It runs in a thread and we talk to it over a real socketpair(), to
# validate interoperability in a semi-realistic setting.
#
# The second is a very weird virtual echo server that lives inside a custom
# Stream class. It lives entirely inside the Python object space; there are no
# operating system calls in it at all. No threads, no I/O, nothing. It's
# 'send_all' call takes encrypted data from a client and feeds it directly into
# the server-side TLS state engine to decrypt, then takes that data, feeds it
# back through to get the encrypted response, and returns it from 'receive_some'. This
# gives us full control and reproducibility. This server is written using
# PyOpenSSL, so that we can trigger renegotiations on demand. It also allows
# us to insert random (virtual) delays, to really exercise all the weird paths
# in SSLStream's state engine.
#
# Both present a certificate for "trio-test-1.example.org".

TRIO_TEST_CA = trustme.CA()
TRIO_TEST_1_CERT = TRIO_TEST_CA.issue_server_cert("trio-test-1.example.org")

SERVER_CTX = stdlib_ssl.create_default_context(stdlib_ssl.Purpose.CLIENT_AUTH)
TRIO_TEST_1_CERT.configure_cert(SERVER_CTX)

CLIENT_CTX = stdlib_ssl.create_default_context()
TRIO_TEST_CA.configure_trust(CLIENT_CTX)


# The blocking socket server.
def ssl_echo_serve_sync(sock, *, expect_fail=False):
    try:
        wrapped = SERVER_CTX.wrap_socket(
            sock, server_side=True, suppress_ragged_eofs=False
        )
        wrapped.do_handshake()
        while True:
            data = wrapped.recv(4096)
            if not data:
                # other side has initiated a graceful shutdown; we try to
                # respond in kind but it's legal for them to have already gone
                # away.
                exceptions = (BrokenPipeError,)
                # Under unclear conditions, CPython sometimes raises
                # SSLWantWriteError here. This is a bug (bpo-32219), but it's
                # not our bug, so ignore it.
                exceptions += (stdlib_ssl.SSLWantWriteError,)
                try:
                    wrapped.unwrap()
                except exceptions:
                    pass
                return
            wrapped.sendall(data)
    except Exception as exc:
        if expect_fail:
            print("ssl_echo_serve_sync got error as expected:", exc)
        else:  # pragma: no cover
            raise
    else:
        if expect_fail:  # pragma: no cover
            raise RuntimeError("failed to fail?")


# Fixture that gives a raw socket connected to a trio-test-1 echo server
# (running in a thread). Useful for testing making connections with different
# SSLContexts.
@asynccontextmanager
@async_generator
async def ssl_echo_server_raw(**kwargs):
    a, b = stdlib_socket.socketpair()
    async with trio.open_nursery() as nursery:
        # Exiting the 'with a, b' context manager closes the sockets, which
        # causes the thread to exit (possibly with an error), which allows the
        # nursery context manager to exit too.
        with a, b:
            nursery.start_soon(
                trio.run_sync_in_worker_thread,
                partial(ssl_echo_serve_sync, b, **kwargs)
            )

            await yield_(SocketStream(tsocket.from_stdlib_socket(a)))


# Fixture that gives a properly set up SSLStream connected to a trio-test-1
# echo server (running in a thread)
@asynccontextmanager
@async_generator
async def ssl_echo_server(**kwargs):
    async with ssl_echo_server_raw(**kwargs) as sock:
        await yield_(
            tssl.SSLStream(
                sock, CLIENT_CTX, server_hostname="trio-test-1.example.org"
            )
        )


# The weird in-memory server ... thing.
# Doesn't inherit from Stream because I left out the methods that we don't
# actually need.
class PyOpenSSLEchoStream:
    def __init__(self, sleeper=None):
        ctx = SSL.Context(SSL.SSLv23_METHOD)
        # TLS 1.3 removes renegotiation support. Which is great for them, but
        # we still have to support versions before that, and that means we
        # need to test renegotation support, which means we need to force this
        # to use a lower version where this test server can trigger
        # renegotiations. Of course TLS 1.3 support isn't released yet, but
        # I'm told that this will work once it is. (And once it is we can
        # remove the pragma: no cover too.) Alternatively, once we drop
        # support for CPython 3.5 on MacOS, then we could switch to using
        # TLSv1_2_METHOD.
        #
        # Discussion: https://github.com/pyca/pyopenssl/issues/624
        if hasattr(SSL, "OP_NO_TLSv1_3"):  # pragma: no cover
            ctx.set_options(SSL.OP_NO_TLSv1_3)
        # Unfortunately there's currently no way to say "use 1.3 or worse", we
        # can only disable specific versions. And if the two sides start
        # negotiating 1.4 at some point in the future, it *might* mean that
        # our tests silently stop working properly. So the next line is a
        # tripwire to remind us we need to revisit this stuff in 5 years or
        # whatever when the next TLS version is released:
        assert not hasattr(SSL, "OP_NO_TLSv1_4")
        TRIO_TEST_1_CERT.configure_cert(ctx)
        self._conn = SSL.Connection(ctx, None)
        self._conn.set_accept_state()
        self._lot = _core.ParkingLot()
        self._pending_cleartext = bytearray()

        self._send_all_conflict_detector = ConflictDetector(
            "simultaneous calls to PyOpenSSLEchoStream.send_all"
        )
        self._receive_some_conflict_detector = ConflictDetector(
            "simultaneous calls to PyOpenSSLEchoStream.receive_some"
        )

        if sleeper is None:

            async def no_op_sleeper(_):
                return

            self.sleeper = no_op_sleeper
        else:
            self.sleeper = sleeper

    async def aclose(self):
        self._conn.bio_shutdown()

    def renegotiate_pending(self):
        return self._conn.renegotiate_pending()

    def renegotiate(self):
        # Returns false if a renegotation is already in progress, meaning
        # nothing happens.
        assert self._conn.renegotiate()

    async def wait_send_all_might_not_block(self):
        async with self._send_all_conflict_detector:
            await _core.checkpoint()
            await self.sleeper("wait_send_all_might_not_block")

    async def send_all(self, data):
        print("  --> transport_stream.send_all")
        async with self._send_all_conflict_detector:
            await _core.checkpoint()
            await self.sleeper("send_all")
            self._conn.bio_write(data)
            while True:
                await self.sleeper("send_all")
                try:
                    data = self._conn.recv(1)
                except SSL.ZeroReturnError:
                    self._conn.shutdown()
                    print("renegotiations:", self._conn.total_renegotiations())
                    break
                except SSL.WantReadError:
                    break
                else:
                    self._pending_cleartext += data
            self._lot.unpark_all()
            await self.sleeper("send_all")
            print("  <-- transport_stream.send_all finished")

    async def receive_some(self, nbytes):
        print("  --> transport_stream.receive_some")
        async with self._receive_some_conflict_detector:
            try:
                await _core.checkpoint()
                while True:
                    await self.sleeper("receive_some")
                    try:
                        return self._conn.bio_read(nbytes)
                    except SSL.WantReadError:
                        # No data in our ciphertext buffer; try to generate
                        # some.
                        if self._pending_cleartext:
                            # We have some cleartext; maybe we can encrypt it
                            # and then return it.
                            print("    trying", self._pending_cleartext)
                            try:
                                # PyOpenSSL bug: doesn't accept bytearray
                                # https://github.com/pyca/pyopenssl/issues/621
                                next_byte = self._pending_cleartext[0:1]
                                self._conn.send(bytes(next_byte))
                            # Apparently this next bit never gets hit in the
                            # test suite, but it's not an interesting omission
                            # so let's pragma it.
                            except SSL.WantReadError:  # pragma: no cover
                                # We didn't manage to send the cleartext (and
                                # in particular we better leave it there to
                                # try again, due to openssl's retry
                                # semantics), but it's possible we pushed a
                                # renegotiation forward and *now* we have data
                                # to send.
                                try:
                                    return self._conn.bio_read(nbytes)
                                except SSL.WantReadError:
                                    # Nope. We're just going to have to wait
                                    # for someone to call send_all() to give
                                    # use more data.
                                    print("parking (a)")
                                    await self._lot.park()
                            else:
                                # We successfully sent that byte, so we don't
                                # have to again.
                                del self._pending_cleartext[0:1]
                        else:
                            # no pending cleartext; nothing to do but wait for
                            # someone to call send_all
                            print("parking (b)")
                            await self._lot.park()
            finally:
                await self.sleeper("receive_some")
                print("  <-- transport_stream.receive_some finished")


async def test_PyOpenSSLEchoStream_gives_resource_busy_errors():
    # Make sure that PyOpenSSLEchoStream complains if two tasks call send_all
    # at the same time, or ditto for receive_some. The tricky cases where SSLStream
    # might accidentally do this are during renegotation, which we test using
    # PyOpenSSLEchoStream, so this makes sure that if we do have a bug then
    # PyOpenSSLEchoStream will notice and complain.

    s = PyOpenSSLEchoStream()
    with pytest.raises(_core.ResourceBusyError) as excinfo:
        async with _core.open_nursery() as nursery:
            nursery.start_soon(s.send_all, b"x")
            nursery.start_soon(s.send_all, b"x")
    assert "simultaneous" in str(excinfo.value)

    s = PyOpenSSLEchoStream()
    with pytest.raises(_core.ResourceBusyError) as excinfo:
        async with _core.open_nursery() as nursery:
            nursery.start_soon(s.send_all, b"x")
            nursery.start_soon(s.wait_send_all_might_not_block)
    assert "simultaneous" in str(excinfo.value)

    s = PyOpenSSLEchoStream()
    with pytest.raises(_core.ResourceBusyError) as excinfo:
        async with _core.open_nursery() as nursery:
            nursery.start_soon(s.wait_send_all_might_not_block)
            nursery.start_soon(s.wait_send_all_might_not_block)
    assert "simultaneous" in str(excinfo.value)

    s = PyOpenSSLEchoStream()
    with pytest.raises(_core.ResourceBusyError) as excinfo:
        async with _core.open_nursery() as nursery:
            nursery.start_soon(s.receive_some, 1)
            nursery.start_soon(s.receive_some, 1)
    assert "simultaneous" in str(excinfo.value)


@contextmanager
def virtual_ssl_echo_server(**kwargs):
    fakesock = PyOpenSSLEchoStream(**kwargs)
    yield tssl.SSLStream(
        fakesock, CLIENT_CTX, server_hostname="trio-test-1.example.org"
    )


def ssl_wrap_pair(
    client_transport, server_transport, *, client_kwargs={}, server_kwargs={}
):
    client_ssl = tssl.SSLStream(
        client_transport,
        CLIENT_CTX,
        server_hostname="trio-test-1.example.org",
        **client_kwargs
    )
    server_ssl = tssl.SSLStream(
        server_transport, SERVER_CTX, server_side=True, **server_kwargs
    )
    return client_ssl, server_ssl


def ssl_memory_stream_pair(**kwargs):
    client_transport, server_transport = memory_stream_pair()
    return ssl_wrap_pair(client_transport, server_transport, **kwargs)


def ssl_lockstep_stream_pair(**kwargs):
    client_transport, server_transport = lockstep_stream_pair()
    return ssl_wrap_pair(client_transport, server_transport, **kwargs)


def test_exports():
    # Just a quick check to make sure _reexport isn't totally broken
    assert hasattr(tssl, "SSLError")
    assert "SSLError" in tssl.__all__

    assert hasattr(tssl, "Purpose")
    assert "Purpose" in tssl.__all__

    # Intentionally omitted
    assert not hasattr(tssl, "SSLContext")


# Simple smoke test for handshake/send/receive/shutdown talking to a
# synchronous server, plus make sure that we do the bare minimum of
# certificate checking (even though this is really Python's responsibility)
async def test_ssl_client_basics():
    # Everything OK
    async with ssl_echo_server() as s:
        assert not s.server_side
        await s.send_all(b"x")
        assert await s.receive_some(1) == b"x"
        await s.aclose()

    # Didn't configure the CA file, should fail
    async with ssl_echo_server_raw(expect_fail=True) as sock:
        client_ctx = stdlib_ssl.create_default_context()
        s = tssl.SSLStream(
            sock, client_ctx, server_hostname="trio-test-1.example.org"
        )
        assert not s.server_side
        with pytest.raises(BrokenStreamError) as excinfo:
            await s.send_all(b"x")
        assert isinstance(excinfo.value.__cause__, tssl.SSLError)

    # Trusted CA, but wrong host name
    async with ssl_echo_server_raw(expect_fail=True) as sock:
        s = tssl.SSLStream(
            sock, CLIENT_CTX, server_hostname="trio-test-2.example.org"
        )
        assert not s.server_side
        with pytest.raises(BrokenStreamError) as excinfo:
            await s.send_all(b"x")
        assert isinstance(excinfo.value.__cause__, tssl.CertificateError)


async def test_ssl_server_basics():
    a, b = stdlib_socket.socketpair()
    with a, b:
        server_sock = tsocket.from_stdlib_socket(b)
        server_transport = tssl.SSLStream(
            SocketStream(server_sock), SERVER_CTX, server_side=True
        )
        assert server_transport.server_side

        def client():
            client_sock = CLIENT_CTX.wrap_socket(
                a, server_hostname="trio-test-1.example.org"
            )
            client_sock.sendall(b"x")
            assert client_sock.recv(1) == b"y"
            client_sock.sendall(b"z")
            client_sock.unwrap()

        t = threading.Thread(target=client)
        t.start()

        assert await server_transport.receive_some(1) == b"x"
        await server_transport.send_all(b"y")
        assert await server_transport.receive_some(1) == b"z"
        assert await server_transport.receive_some(1) == b""
        await server_transport.aclose()

        t.join()


async def test_attributes():
    async with ssl_echo_server_raw(expect_fail=True) as sock:
        good_ctx = CLIENT_CTX
        bad_ctx = stdlib_ssl.create_default_context()
        s = tssl.SSLStream(
            sock, good_ctx, server_hostname="trio-test-1.example.org"
        )

        assert s.transport_stream is sock

        # Forwarded attribute getting
        assert s.context is good_ctx
        assert s.server_side == False
        assert s.server_hostname == "trio-test-1.example.org"
        with pytest.raises(AttributeError):
            s.asfdasdfsa

        # __dir__
        assert "transport_stream" in dir(s)
        assert "context" in dir(s)

        # Setting the attribute goes through to the underlying object

        # most attributes on SSLObject are read-only
        with pytest.raises(AttributeError):
            s.server_side = True
        with pytest.raises(AttributeError):
            s.server_hostname = "asdf"

        # but .context is *not*. Check that we forward attribute setting by
        # making sure that after we set the bad context our handshake indeed
        # fails:
        s.context = bad_ctx
        assert s.context is bad_ctx
        with pytest.raises(BrokenStreamError) as excinfo:
            await s.do_handshake()
        assert isinstance(excinfo.value.__cause__, tssl.SSLError)


# Note: this test fails horribly if we force TLS 1.2 and trigger a
# renegotiation at the beginning (e.g. by switching to the pyopenssl
# server). Usually the client crashes in SSLObject.write with "UNEXPECTED
# RECORD"; sometimes we get something more exotic like a SyscallError. This is
# odd because openssl isn't doing any syscalls, but so it goes. After lots of
# websearching I'm pretty sure this is due to a bug in OpenSSL, where it just
# can't reliably handle full-duplex communication combined with
# renegotiation. Nice, eh?
#
#   https://rt.openssl.org/Ticket/Display.html?id=3712
#   https://rt.openssl.org/Ticket/Display.html?id=2481
#   http://openssl.6102.n7.nabble.com/TLS-renegotiation-failure-on-receiving-application-data-during-handshake-td48127.html
#   https://stackoverflow.com/questions/18728355/ssl-renegotiation-with-full-duplex-socket-communication
#
# In some variants of this test (maybe only against the java server?) I've
# also seen cases where our send_all blocks waiting to write, and then our receive_some
# also blocks waiting to write, and they never wake up again. It looks like
# some kind of deadlock. I suspect there may be an issue where we've filled up
# the send buffers, and the remote side is trying to handle the renegotiation
# from inside a write() call, so it has a problem: there's all this application
# data clogging up the pipe, but it can't process and return it to the
# application because it's in write(), and it doesn't want to buffer infinite
# amounts of data, and... actually I guess those are the only two choices.
#
# NSS even documents that you shouldn't try to do a renegotiation except when
# the connection is idle:
#
#   https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/SSL_functions/sslfnc.html#1061582
#
# I begin to see why HTTP/2 forbids renegotiation and TLS 1.3 removes it...


async def test_full_duplex_basics():
    CHUNKS = 30
    CHUNK_SIZE = 32768
    EXPECTED = CHUNKS * CHUNK_SIZE

    sent = bytearray()
    received = bytearray()

    async def sender(s):
        nonlocal sent
        for i in range(CHUNKS):
            print(i)
            chunk = bytes([i] * CHUNK_SIZE)
            sent += chunk
            await s.send_all(chunk)

    async def receiver(s):
        nonlocal received
        while len(received) < EXPECTED:
            chunk = await s.receive_some(CHUNK_SIZE // 2)
            received += chunk

    async with ssl_echo_server() as s:
        async with _core.open_nursery() as nursery:
            nursery.start_soon(sender, s)
            nursery.start_soon(receiver, s)
            # And let's have some doing handshakes too, everyone
            # simultaneously
            nursery.start_soon(s.do_handshake)
            nursery.start_soon(s.do_handshake)

        await s.aclose()

    assert len(sent) == len(received) == EXPECTED
    assert sent == received


async def test_renegotiation_simple():
    with virtual_ssl_echo_server() as s:
        await s.do_handshake()

        s.transport_stream.renegotiate()
        await s.send_all(b"a")
        assert await s.receive_some(1) == b"a"

        # Have to send some more data back and forth to make sure the
        # renegotiation is finished before shutting down the
        # connection... otherwise openssl raises an error. I think this is a
        # bug in openssl but what can ya do.
        await s.send_all(b"b")
        assert await s.receive_some(1) == b"b"

        await s.aclose()


@slow
async def test_renegotiation_randomized(mock_clock):
    # The only blocking things in this function are our random sleeps, so 0 is
    # a good threshold.
    mock_clock.autojump_threshold = 0

    import random
    r = random.Random(0)

    async def sleeper(_):
        await trio.sleep(r.uniform(0, 10))

    async def clear():
        while s.transport_stream.renegotiate_pending():
            with assert_checkpoints():
                await send(b"-")
            with assert_checkpoints():
                await expect(b"-")
        print("-- clear --")

    async def send(byte):
        await s.transport_stream.sleeper("outer send")
        print("calling SSLStream.send_all", byte)
        with assert_checkpoints():
            await s.send_all(byte)

    async def expect(expected):
        await s.transport_stream.sleeper("expect")
        print("calling SSLStream.receive_some, expecting", expected)
        assert len(expected) == 1
        with assert_checkpoints():
            assert await s.receive_some(1) == expected

    with virtual_ssl_echo_server(sleeper=sleeper) as s:
        await s.do_handshake()

        await send(b"a")
        s.transport_stream.renegotiate()
        await expect(b"a")

        await clear()

        for i in range(100):
            b1 = bytes([i % 0xff])
            b2 = bytes([(2 * i) % 0xff])
            s.transport_stream.renegotiate()
            async with _core.open_nursery() as nursery:
                nursery.start_soon(send, b1)
                nursery.start_soon(expect, b1)
            async with _core.open_nursery() as nursery:
                nursery.start_soon(expect, b2)
                nursery.start_soon(send, b2)
            await clear()

        for i in range(100):
            b1 = bytes([i % 0xff])
            b2 = bytes([(2 * i) % 0xff])
            await send(b1)
            s.transport_stream.renegotiate()
            await expect(b1)
            async with _core.open_nursery() as nursery:
                nursery.start_soon(expect, b2)
                nursery.start_soon(send, b2)
            await clear()

    # Checking that wait_send_all_might_not_block and receive_some don't
    # conflict:

    # 1) Set up a situation where expect (receive_some) is blocked sending,
    # and wait_send_all_might_not_block comes in.

    # Our receive_some() call will get stuck when it hits send_all
    async def sleeper_with_slow_send_all(method):
        if method == "send_all":
            await trio.sleep(100000)

    # And our wait_send_all_might_not_block call will give it time to get
    # stuck, and then start
    async def sleep_then_wait_writable():
        await trio.sleep(1000)
        await s.wait_send_all_might_not_block()

    with virtual_ssl_echo_server(sleeper=sleeper_with_slow_send_all) as s:
        await send(b"x")
        s.transport_stream.renegotiate()
        async with _core.open_nursery() as nursery:
            nursery.start_soon(expect, b"x")
            nursery.start_soon(sleep_then_wait_writable)

        await clear()

        await s.aclose()

    # 2) Same, but now wait_send_all_might_not_block is stuck when
    # receive_some tries to send.

    async def sleeper_with_slow_wait_writable_and_expect(method):
        if method == "wait_send_all_might_not_block":
            await trio.sleep(100000)
        elif method == "expect":
            await trio.sleep(1000)

    with virtual_ssl_echo_server(
        sleeper=sleeper_with_slow_wait_writable_and_expect
    ) as s:
        await send(b"x")
        s.transport_stream.renegotiate()
        async with _core.open_nursery() as nursery:
            nursery.start_soon(expect, b"x")
            nursery.start_soon(s.wait_send_all_might_not_block)

        await clear()

        await s.aclose()


async def test_resource_busy_errors():
    async def do_send_all():
        with assert_checkpoints():
            await s.send_all(b"x")

    async def do_receive_some():
        with assert_checkpoints():
            await s.receive_some(1)

    async def do_wait_send_all_might_not_block():
        with assert_checkpoints():
            await s.wait_send_all_might_not_block()

    s, _ = ssl_lockstep_stream_pair()
    with pytest.raises(_core.ResourceBusyError) as excinfo:
        async with _core.open_nursery() as nursery:
            nursery.start_soon(do_send_all)
            nursery.start_soon(do_send_all)
    assert "another task" in str(excinfo.value)

    s, _ = ssl_lockstep_stream_pair()
    with pytest.raises(_core.ResourceBusyError) as excinfo:
        async with _core.open_nursery() as nursery:
            nursery.start_soon(do_receive_some)
            nursery.start_soon(do_receive_some)
    assert "another task" in str(excinfo.value)

    s, _ = ssl_lockstep_stream_pair()
    with pytest.raises(_core.ResourceBusyError) as excinfo:
        async with _core.open_nursery() as nursery:
            nursery.start_soon(do_send_all)
            nursery.start_soon(do_wait_send_all_might_not_block)
    assert "another task" in str(excinfo.value)

    s, _ = ssl_lockstep_stream_pair()
    with pytest.raises(_core.ResourceBusyError) as excinfo:
        async with _core.open_nursery() as nursery:
            nursery.start_soon(do_wait_send_all_might_not_block)
            nursery.start_soon(do_wait_send_all_might_not_block)
    assert "another task" in str(excinfo.value)


async def test_wait_writable_calls_underlying_wait_writable():
    record = []

    class NotAStream:
        async def wait_send_all_might_not_block(self):
            record.append("ok")

    ctx = stdlib_ssl.create_default_context()
    s = tssl.SSLStream(NotAStream(), ctx, server_hostname="x")
    await s.wait_send_all_might_not_block()
    assert record == ["ok"]


async def test_checkpoints():
    async with ssl_echo_server() as s:
        with assert_checkpoints():
            await s.do_handshake()
        with assert_checkpoints():
            await s.do_handshake()
        with assert_checkpoints():
            await s.wait_send_all_might_not_block()
        with assert_checkpoints():
            await s.send_all(b"xxx")
        with assert_checkpoints():
            await s.receive_some(1)
        # These receive_some's in theory could return immediately, because the
        # "xxx" was sent in a single record and after the first
        # receive_some(1) the rest are sitting inside the SSLObject's internal
        # buffers.
        with assert_checkpoints():
            await s.receive_some(1)
        with assert_checkpoints():
            await s.receive_some(1)
        with assert_checkpoints():
            await s.unwrap()

    async with ssl_echo_server() as s:
        await s.do_handshake()
        with assert_checkpoints():
            await s.aclose()


async def test_send_all_empty_string():
    async with ssl_echo_server() as s:
        await s.do_handshake()

        # underlying SSLObject interprets writing b"" as indicating an EOF,
        # for some reason. Make sure we don't inherit this.
        with assert_checkpoints():
            await s.send_all(b"")
        with assert_checkpoints():
            await s.send_all(b"")
        await s.send_all(b"x")
        assert await s.receive_some(1) == b"x"

        await s.aclose()


@pytest.mark.parametrize("https_compatible", [False, True])
async def test_SSLStream_generic(https_compatible):
    async def stream_maker():
        return ssl_memory_stream_pair(
            client_kwargs={"https_compatible": https_compatible},
            server_kwargs={"https_compatible": https_compatible},
        )

    async def clogged_stream_maker():
        client, server = ssl_lockstep_stream_pair()
        # If we don't do handshakes up front, then we run into a problem in
        # the following situation:
        # - server does wait_send_all_might_not_block
        # - client does receive_some to unclog it
        # Then the client's receive_some will actually send some data to start
        # the handshake, and itself get stuck.
        async with _core.open_nursery() as nursery:
            nursery.start_soon(client.do_handshake)
            nursery.start_soon(server.do_handshake)
        return client, server

    await check_two_way_stream(stream_maker, clogged_stream_maker)


async def test_unwrap():
    client_ssl, server_ssl = ssl_memory_stream_pair()
    client_transport = client_ssl.transport_stream
    server_transport = server_ssl.transport_stream

    seq = Sequencer()

    async def client():
        await client_ssl.do_handshake()
        await client_ssl.send_all(b"x")
        assert await client_ssl.receive_some(1) == b"y"
        await client_ssl.send_all(b"z")

        # After sending that, disable outgoing data from our end, to make
        # sure the server doesn't see our EOF until after we've sent some
        # trailing data
        async with seq(0):
            send_all_hook = client_transport.send_stream.send_all_hook
            client_transport.send_stream.send_all_hook = None

        assert await client_ssl.receive_some(1) == b""
        assert client_ssl.transport_stream is client_transport
        # We just received EOF. Unwrap the connection and send some more.
        raw, trailing = await client_ssl.unwrap()
        assert raw is client_transport
        assert trailing == b""
        assert client_ssl.transport_stream is None
        await raw.send_all(b"trailing")

        # Reconnect the streams. Now the server will receive both our shutdown
        # acknowledgement + the trailing data in a single lump.
        client_transport.send_stream.send_all_hook = send_all_hook
        await client_transport.send_stream.send_all_hook()

    async def server():
        await server_ssl.do_handshake()
        assert await server_ssl.receive_some(1) == b"x"
        await server_ssl.send_all(b"y")
        assert await server_ssl.receive_some(1) == b"z"
        # Now client is blocked waiting for us to send something, but
        # instead we close the TLS connection (with sequencer to make sure
        # that the client won't see and automatically respond before we've had
        # a chance to disable the client->server transport)
        async with seq(1):
            raw, trailing = await server_ssl.unwrap()
        assert raw is server_transport
        assert trailing == b"trailing"
        assert server_ssl.transport_stream is None

    async with _core.open_nursery() as nursery:
        nursery.start_soon(client)
        nursery.start_soon(server)


async def test_closing_nice_case():
    # the nice case: graceful closes all around

    client_ssl, server_ssl = ssl_memory_stream_pair()
    client_transport = client_ssl.transport_stream

    # Both the handshake and the close require back-and-forth discussion, so
    # we need to run them concurrently
    async def client_closer():
        with assert_checkpoints():
            await client_ssl.aclose()

    async def server_closer():
        assert await server_ssl.receive_some(10) == b""
        assert await server_ssl.receive_some(10) == b""
        with assert_checkpoints():
            await server_ssl.aclose()

    async with _core.open_nursery() as nursery:
        nursery.start_soon(client_closer)
        nursery.start_soon(server_closer)

    # closing the SSLStream also closes its transport
    with pytest.raises(ClosedResourceError):
        await client_transport.send_all(b"123")

    # once closed, it's OK to close again
    with assert_checkpoints():
        await client_ssl.aclose()
    with assert_checkpoints():
        await client_ssl.aclose()

    # Trying to send more data does not work
    with assert_checkpoints():
        with pytest.raises(ClosedResourceError):
            await server_ssl.send_all(b"123")

    # And once the connection is has been closed *locally*, then instead of
    # getting empty bytestrings we get a proper error
    with assert_checkpoints():
        with pytest.raises(ClosedResourceError):
            await client_ssl.receive_some(10) == b""

    with assert_checkpoints():
        with pytest.raises(ClosedResourceError):
            await client_ssl.unwrap()

    with assert_checkpoints():
        with pytest.raises(ClosedResourceError):
            await client_ssl.do_handshake()

    # Check that a graceful close *before* handshaking gives a clean EOF on
    # the other side
    client_ssl, server_ssl = ssl_memory_stream_pair()

    async def expect_eof_server():
        with assert_checkpoints():
            assert await server_ssl.receive_some(10) == b""
        with assert_checkpoints():
            await server_ssl.aclose()

    async with _core.open_nursery() as nursery:
        nursery.start_soon(client_ssl.aclose)
        nursery.start_soon(expect_eof_server)


async def test_send_all_fails_in_the_middle():
    client, server = ssl_memory_stream_pair()

    async with _core.open_nursery() as nursery:
        nursery.start_soon(client.do_handshake)
        nursery.start_soon(server.do_handshake)

    async def bad_hook():
        raise KeyError

    client.transport_stream.send_stream.send_all_hook = bad_hook

    with pytest.raises(KeyError):
        await client.send_all(b"x")

    with pytest.raises(BrokenStreamError):
        await client.wait_send_all_might_not_block()

    closed = 0

    def close_hook():
        nonlocal closed
        closed += 1

    client.transport_stream.send_stream.close_hook = close_hook
    client.transport_stream.receive_stream.close_hook = close_hook
    await client.aclose()

    assert closed == 2


async def test_ssl_over_ssl():
    client_0, server_0 = memory_stream_pair()

    client_1 = tssl.SSLStream(
        client_0, CLIENT_CTX, server_hostname="trio-test-1.example.org"
    )
    server_1 = tssl.SSLStream(server_0, SERVER_CTX, server_side=True)

    client_2 = tssl.SSLStream(
        client_1, CLIENT_CTX, server_hostname="trio-test-1.example.org"
    )
    server_2 = tssl.SSLStream(server_1, SERVER_CTX, server_side=True)

    async def client():
        await client_2.send_all(b"hi")
        assert await client_2.receive_some(10) == b"bye"

    async def server():
        assert await server_2.receive_some(10) == b"hi"
        await server_2.send_all(b"bye")

    async with _core.open_nursery() as nursery:
        nursery.start_soon(client)
        nursery.start_soon(server)


async def test_ssl_bad_shutdown():
    client, server = ssl_memory_stream_pair()

    async with _core.open_nursery() as nursery:
        nursery.start_soon(client.do_handshake)
        nursery.start_soon(server.do_handshake)

    await trio.aclose_forcefully(client)
    # now the server sees a broken stream
    with pytest.raises(BrokenStreamError):
        await server.receive_some(10)
    with pytest.raises(BrokenStreamError):
        await server.send_all(b"x" * 10)

    await server.aclose()


async def test_ssl_bad_shutdown_but_its_ok():
    client, server = ssl_memory_stream_pair(
        server_kwargs={"https_compatible": True},
        client_kwargs={
            "https_compatible": True
        }
    )

    async with _core.open_nursery() as nursery:
        nursery.start_soon(client.do_handshake)
        nursery.start_soon(server.do_handshake)

    await trio.aclose_forcefully(client)
    # the server sees that as a clean shutdown
    assert await server.receive_some(10) == b""
    with pytest.raises(BrokenStreamError):
        await server.send_all(b"x" * 10)

    await server.aclose()


async def test_ssl_handshake_failure_during_aclose():
    # Weird scenario: aclose() triggers an automatic handshake, and this
    # fails. This also exercises a bit of code in aclose() that was otherwise
    # uncovered, for re-raising exceptions after calling aclose_forcefully on
    # the underlying transport.
    async with ssl_echo_server_raw(expect_fail=True) as sock:
        # Don't configure trust correctly
        client_ctx = stdlib_ssl.create_default_context()
        s = tssl.SSLStream(
            sock, client_ctx, server_hostname="trio-test-1.example.org"
        )
        # It's a little unclear here whether aclose should swallow the error
        # or let it escape. We *do* swallow the error if it arrives when we're
        # sending close_notify, because both sides closing the connection
        # simultaneously is allowed. But I guess when https_compatible=False
        # then it's bad if we can get through a whole connection with a peer
        # that has no valid certificate, and never raise an error.
        with pytest.raises(BrokenStreamError) as excinfo:
            await s.aclose()


async def test_ssl_only_closes_stream_once():
    # We used to have a bug where if transport_stream.aclose() raised an
    # error, we would call it again. This checks that that's fixed.
    client, server = ssl_memory_stream_pair()

    async with _core.open_nursery() as nursery:
        nursery.start_soon(client.do_handshake)
        nursery.start_soon(server.do_handshake)

    client_orig_close_hook = client.transport_stream.send_stream.close_hook
    transport_close_count = 0

    def close_hook():
        nonlocal transport_close_count
        client_orig_close_hook()
        transport_close_count += 1
        raise KeyError

    client.transport_stream.send_stream.close_hook = close_hook

    with pytest.raises(KeyError):
        await client.aclose()
    assert transport_close_count == 1


async def test_ssl_https_compatibility_disagreement():
    client, server = ssl_memory_stream_pair(
        server_kwargs={"https_compatible": False},
        client_kwargs={
            "https_compatible": True
        }
    )

    async with _core.open_nursery() as nursery:
        nursery.start_soon(client.do_handshake)
        nursery.start_soon(server.do_handshake)

    # client is in HTTPS-mode, server is not
    # so client doing graceful_shutdown causes an error on server
    async def receive_and_expect_error():
        with pytest.raises(BrokenStreamError) as excinfo:
            await server.receive_some(10)
        assert isinstance(excinfo.value.__cause__, tssl.SSLEOFError)

    async with _core.open_nursery() as nursery:
        nursery.start_soon(client.aclose)
        nursery.start_soon(receive_and_expect_error)


async def test_https_mode_eof_before_handshake():
    client, server = ssl_memory_stream_pair(
        server_kwargs={"https_compatible": True},
        client_kwargs={
            "https_compatible": True
        }
    )

    async def server_expect_clean_eof():
        assert await server.receive_some(10) == b""

    async with _core.open_nursery() as nursery:
        nursery.start_soon(client.aclose)
        nursery.start_soon(server_expect_clean_eof)


async def test_send_error_during_handshake():
    client, server = ssl_memory_stream_pair()

    async def bad_hook():
        raise KeyError

    client.transport_stream.send_stream.send_all_hook = bad_hook

    with pytest.raises(KeyError):
        with assert_checkpoints():
            await client.do_handshake()

    with pytest.raises(BrokenStreamError):
        with assert_checkpoints():
            await client.do_handshake()


async def test_receive_error_during_handshake():
    client, server = ssl_memory_stream_pair()

    async def bad_hook():
        raise KeyError

    client.transport_stream.receive_stream.receive_some_hook = bad_hook

    async def client_side(cancel_scope):
        with pytest.raises(KeyError):
            with assert_checkpoints():
                await client.do_handshake()
        cancel_scope.cancel()

    async with _core.open_nursery() as nursery:
        nursery.start_soon(client_side, nursery.cancel_scope)
        nursery.start_soon(server.do_handshake)

    with pytest.raises(BrokenStreamError):
        with assert_checkpoints():
            await client.do_handshake()


async def test_getpeercert():
    # Make sure we're not affected by https://bugs.python.org/issue29334
    client, server = ssl_memory_stream_pair()

    async with _core.open_nursery() as nursery:
        nursery.start_soon(client.do_handshake)
        nursery.start_soon(server.do_handshake)

    assert server.getpeercert() is None
    print(client.getpeercert())
    assert (
        ("DNS",
         "trio-test-1.example.org") in client.getpeercert()["subjectAltName"]
    )


async def test_SSLListener():
    async def setup(**kwargs):
        listen_sock = tsocket.socket()
        await listen_sock.bind(("127.0.0.1", 0))
        listen_sock.listen(1)
        socket_listener = SocketListener(listen_sock)
        ssl_listener = tssl.SSLListener(socket_listener, SERVER_CTX, **kwargs)

        transport_client = await open_tcp_stream(*listen_sock.getsockname())
        ssl_client = tssl.SSLStream(
            transport_client,
            CLIENT_CTX,
            server_hostname="trio-test-1.example.org"
        )
        return listen_sock, ssl_listener, ssl_client

    listen_sock, ssl_listener, ssl_client = await setup()

    async with ssl_client:
        ssl_server = await ssl_listener.accept()

        async with ssl_server:
            assert not ssl_server._https_compatible

            # Make sure the connection works
            async with _core.open_nursery() as nursery:
                nursery.start_soon(ssl_client.do_handshake)
                nursery.start_soon(ssl_server.do_handshake)

        # Test SSLListener.aclose
        await ssl_listener.aclose()
        assert listen_sock.fileno() == -1

    ################

    # Test https_compatible and max_refill_bytes
    _, ssl_listener, ssl_client = await setup(
        https_compatible=True,
        max_refill_bytes=100,
    )

    ssl_server = await ssl_listener.accept()

    assert ssl_server._https_compatible
    assert ssl_server._max_refill_bytes == 100

    await aclose_forcefully(ssl_listener)
    await aclose_forcefully(ssl_client)
    await aclose_forcefully(ssl_server)
