import pytest

import attr

import trio
from trio.socket import AF_INET, AF_INET6, SOCK_STREAM, IPPROTO_TCP
from trio._highlevel_open_tcp_stream import (
    reorder_for_rfc_6555_section_5_4,
    close_on_error,
    open_tcp_stream,
    format_host_port,
)


def test_close_on_error():
    class CloseMe:
        closed = False

        def close(self):
            self.closed = True

    with close_on_error(CloseMe()) as c:
        pass
    assert not c.closed

    with pytest.raises(RuntimeError):
        with close_on_error(CloseMe()) as c:
            raise RuntimeError
    assert c.closed


def test_reorder_for_rfc_6555_section_5_4():
    def fake4(i):
        return (
            AF_INET, SOCK_STREAM, IPPROTO_TCP, "", ("10.0.0.{}".format(i), 80)
        )

    def fake6(i):
        return (AF_INET6, SOCK_STREAM, IPPROTO_TCP, "", ("::{}".format(i), 80))

    for fake in fake4, fake6:
        # No effect on homogenous lists
        targets = [fake(0), fake(1), fake(2)]
        reorder_for_rfc_6555_section_5_4(targets)
        assert targets == [fake(0), fake(1), fake(2)]

        # Single item lists also OK
        targets = [fake(0)]
        reorder_for_rfc_6555_section_5_4(targets)
        assert targets == [fake(0)]

    # If the list starts out with different families in positions 0 and 1,
    # then it's left alone
    orig = [fake4(0), fake6(0), fake4(1), fake6(1)]
    targets = list(orig)
    reorder_for_rfc_6555_section_5_4(targets)
    assert targets == orig

    # If not, it's reordered
    targets = [fake4(0), fake4(1), fake4(2), fake6(0), fake6(1)]
    reorder_for_rfc_6555_section_5_4(targets)
    assert targets == [fake4(0), fake6(0), fake4(1), fake4(2), fake6(1)]


def test_format_host_port():
    assert format_host_port("127.0.0.1", 80) == "127.0.0.1:80"
    assert format_host_port("example.com", 443) == "example.com:443"
    assert format_host_port("::1", "http") == "[::1]:http"


# Make sure we can connect to localhost using real kernel sockets
async def test_open_tcp_stream_real_socket_smoketest():
    listen_sock = trio.socket.socket()
    await listen_sock.bind(("127.0.0.1", 0))
    _, listen_port = listen_sock.getsockname()
    listen_sock.listen(1)
    client_stream = await open_tcp_stream("127.0.0.1", listen_port)
    server_sock, _ = await listen_sock.accept()
    await client_stream.send_all(b"x")
    assert await server_sock.recv(1) == b"x"
    await client_stream.aclose()
    server_sock.close()

    listen_sock.close()


async def test_open_tcp_stream_input_validation():
    with pytest.raises(ValueError):
        await open_tcp_stream(None, 80)
    with pytest.raises(TypeError):
        await open_tcp_stream("127.0.0.1", b"80")


# Now, thorough tests using fake sockets


@attr.s
class FakeSocket(trio.socket.SocketType):
    scenario = attr.ib()
    family = attr.ib()
    type = attr.ib()
    proto = attr.ib()

    ip = attr.ib(default=None)
    port = attr.ib(default=None)
    succeeded = attr.ib(default=False)
    closed = attr.ib(default=False)

    async def connect(self, sockaddr):
        self.ip = sockaddr[0]
        self.port = sockaddr[1]
        assert self.ip not in self.scenario.sockets
        self.scenario.sockets[self.ip] = self
        self.scenario.connect_times[self.ip] = trio.current_time()
        delay, result = self.scenario.ip_dict[self.ip]
        await trio.sleep(delay)
        if result == "error":
            raise OSError("sorry")
        self.succeeded = True

    def close(self):
        self.closed = True

    # Some stubs to stop SocketStream from complaining:
    def setsockopt(self, *args, **kwargs):
        pass

    def getpeername(self):
        return (self.ip, self.port)


class Scenario(trio.abc.SocketFactory, trio.abc.HostnameResolver):
    def __init__(self, port, ip_list, ipv6_supported):
        # ip_list have to be unique
        ip_order = [ip for (ip, _, _) in ip_list]
        assert len(set(ip_order)) == len(ip_list)
        ip_dict = {}
        for ip, delay, result in ip_list:
            assert 0 <= delay
            assert result in ["error", "success"]
            ip_dict[ip] = (delay, result)

        self.port = port
        self.ip_order = ip_order
        self.ip_dict = ip_dict
        self.ipv6_supported = ipv6_supported
        self.socket_count = 0
        self.sockets = {}
        self.connect_times = {}

    def socket(self, family, type, proto):
        if not self.ipv6_supported and family == trio.socket.AF_INET6:
            raise OSError("pretending not to support ipv6")
        self.socket_count += 1
        return FakeSocket(self, family, type, proto)

    def _ip_to_gai_entry(self, ip):
        if ":" in ip:
            family = trio.socket.AF_INET6
            sockaddr = (ip, self.port, 0, 0)
        else:
            family = trio.socket.AF_INET
            sockaddr = (ip, self.port)
        return (family, SOCK_STREAM, IPPROTO_TCP, "", sockaddr)

    async def getaddrinfo(self, host, port, family, type, proto, flags):
        assert host == b"test.example.com"
        assert port == self.port
        assert family == trio.socket.AF_UNSPEC
        assert type == trio.socket.SOCK_STREAM
        assert proto == 0
        assert flags == 0
        return [self._ip_to_gai_entry(ip) for ip in self.ip_order]

    async def getnameinfo(self, sockaddr, flags):  # pragma: no cover
        raise NotImplementedError

    def check(self, succeeded):
        # sockets only go into self.sockets when connect is called; make sure
        # all the sockets that were created did in fact go in there.
        assert self.socket_count == len(self.sockets)

        for ip, socket in self.sockets.items():
            assert ip in self.ip_dict
            if socket is not succeeded:
                assert socket.closed
            assert socket.port == self.port


async def run_scenario(
    # The port to connect to
    port,
    # A list of
    #  (ip, delay, result)
    # tuples, where delay is in seconds and result is "success" or "error"
    # The ip's will be returned from getaddrinfo in this order, and then
    # connect() calls to them will have the given result.
    ip_list,
    *,
    # If False, AF_INET6 sockets error out on creation, before connect is
    # even called.
    ipv6_supported=True,
    # Normally, we return (winning_sock, scenario object)
    # If this is True, we require there to be an exception, and return
    #   (exception, scenario object)
    expect_error=(),
    **kwargs
):
    scenario = Scenario(port, ip_list, ipv6_supported)
    trio.socket.set_custom_hostname_resolver(scenario)
    trio.socket.set_custom_socket_factory(scenario)

    try:
        stream = await open_tcp_stream("test.example.com", port, **kwargs)
        assert expect_error == ()
        scenario.check(stream.socket)
        return (stream.socket, scenario)
    except AssertionError:  # pragma: no cover
        raise
    except expect_error as exc:
        scenario.check(None)
        return (exc, scenario)


async def test_one_host_quick_success(autojump_clock):
    sock, scenario = await run_scenario(80, [("1.2.3.4", 0.123, "success")])
    assert sock.ip == "1.2.3.4"
    assert trio.current_time() == 0.123


async def test_one_host_slow_success(autojump_clock):
    sock, scenario = await run_scenario(81, [("1.2.3.4", 100, "success")])
    assert sock.ip == "1.2.3.4"
    assert trio.current_time() == 100


async def test_one_host_quick_fail(autojump_clock):
    exc, scenario = await run_scenario(
        82, [("1.2.3.4", 0.123, "error")], expect_error=OSError
    )
    assert isinstance(exc, OSError)
    assert trio.current_time() == 0.123


async def test_one_host_slow_fail(autojump_clock):
    exc, scenario = await run_scenario(
        83, [("1.2.3.4", 100, "error")], expect_error=OSError
    )
    assert isinstance(exc, OSError)
    assert trio.current_time() == 100


# With the default 0.300 second delay, the third attempt will win
async def test_basic_fallthrough(autojump_clock):
    sock, scenario = await run_scenario(
        80,
        [
            ("1.1.1.1", 1, "success"),
            ("2.2.2.2", 1, "success"),
            ("3.3.3.3", 0.2, "success"),
        ],
    )
    assert sock.ip == "3.3.3.3"
    assert trio.current_time() == (0.300 + 0.300 + 0.2)
    assert scenario.connect_times == {
        "1.1.1.1": 0,
        "2.2.2.2": 0.300,
        "3.3.3.3": 0.600,
    }


async def test_early_success(autojump_clock):
    sock, scenario = await run_scenario(
        80,
        [
            ("1.1.1.1", 1, "success"),
            ("2.2.2.2", 0.1, "success"),
            ("3.3.3.3", 0.2, "success"),
        ],
    )
    assert sock.ip == "2.2.2.2"
    assert trio.current_time() == (0.300 + 0.1)
    assert scenario.connect_times == {
        "1.1.1.1": 0,
        "2.2.2.2": 0.300,
        # 3.3.3.3 was never even started
    }


# With a 0.450 second delay, the first attempt will win
async def test_custom_delay(autojump_clock):
    sock, scenario = await run_scenario(
        80,
        [
            ("1.1.1.1", 1, "success"),
            ("2.2.2.2", 1, "success"),
            ("3.3.3.3", 0.2, "success"),
        ],
        happy_eyeballs_delay=0.450,
    )
    assert sock.ip == "1.1.1.1"
    assert trio.current_time() == 1
    assert scenario.connect_times == {
        "1.1.1.1": 0,
        "2.2.2.2": 0.450,
        "3.3.3.3": 0.900,
    }


async def test_custom_errors_expedite(autojump_clock):
    sock, scenario = await run_scenario(
        80,
        [
            ("1.1.1.1", 0.1, "error"),
            ("2.2.2.2", 0.2, "error"),
            ("3.3.3.3", 10, "success"),
            ("4.4.4.4", 0.3, "success"),
        ],
    )
    assert sock.ip == "4.4.4.4"
    assert trio.current_time() == (0.1 + 0.2 + 0.3 + 0.3)
    assert scenario.connect_times == {
        "1.1.1.1": 0,
        "2.2.2.2": 0.1,
        "3.3.3.3": 0.1 + 0.2,
        "4.4.4.4": 0.1 + 0.2 + 0.3,
    }


async def test_all_fail(autojump_clock):
    exc, scenario = await run_scenario(
        80,
        [
            ("1.1.1.1", 0.1, "error"),
            ("2.2.2.2", 0.2, "error"),
            ("3.3.3.3", 10, "error"),
            ("4.4.4.4", 0.3, "error"),
        ],
        expect_error=OSError,
    )
    assert isinstance(exc, OSError)
    assert isinstance(exc.__cause__, trio.MultiError)
    assert len(exc.__cause__.exceptions) == 4
    assert trio.current_time() == (0.1 + 0.2 + 10)
    assert scenario.connect_times == {
        "1.1.1.1": 0,
        "2.2.2.2": 0.1,
        "3.3.3.3": 0.1 + 0.2,
        "4.4.4.4": 0.1 + 0.2 + 0.3,
    }


async def test_multi_success(autojump_clock):
    sock, scenario = await run_scenario(
        80,
        [
            ("1.1.1.1", 0.5, "error"),
            ("2.2.2.2", 10, "success"),
            ("3.3.3.3", 10 - 1, "success"),
            ("4.4.4.4", 10 - 2, "success"),
            ("5.5.5.5", 0.5, "error"),
        ],
        happy_eyeballs_delay=1,
    )
    assert not scenario.sockets["1.1.1.1"].succeeded
    assert scenario.sockets["2.2.2.2"].succeeded
    assert scenario.sockets["3.3.3.3"].succeeded
    assert scenario.sockets["4.4.4.4"].succeeded
    assert not scenario.sockets["5.5.5.5"].succeeded
    assert sock.ip in ["2.2.2.2", "3.3.3.3", "4.4.4.4"]
    assert trio.current_time() == (0.5 + 10)
    assert scenario.connect_times == {
        "1.1.1.1": 0,
        "2.2.2.2": 0.5,
        "3.3.3.3": 1.5,
        "4.4.4.4": 2.5,
        "5.5.5.5": 3.5,
    }


async def test_does_reorder(autojump_clock):
    sock, scenario = await run_scenario(
        80,
        [
            ("1.1.1.1", 10, "error"),
            # This would win if we tried it first...
            ("2.2.2.2", 1, "success"),
            # But in fact we try this first, because of section 5.4
            ("::3", 0.5, "success"),
        ],
        happy_eyeballs_delay=1,
    )
    assert sock.ip == "::3"
    assert trio.current_time() == 1 + 0.5
    assert scenario.connect_times == {
        "1.1.1.1": 0,
        "::3": 1,
    }


async def test_handles_no_ipv6(autojump_clock):
    sock, scenario = await run_scenario(
        80,
        # Here the ipv6 addresses fail at socket creation time, so the connect
        # configuration doesn't matter
        [
            ("::1", 0, "success"),
            ("2.2.2.2", 10, "success"),
            ("::3", 0, "success"),
            ("4.4.4.4", 0.1, "success"),
        ],
        happy_eyeballs_delay=1,
        ipv6_supported=False,
    )
    assert sock.ip == "4.4.4.4"
    assert trio.current_time() == 1 + 0.1
    assert scenario.connect_times == {
        "2.2.2.2": 0,
        "4.4.4.4": 1.0,
    }


async def test_no_hosts(autojump_clock):
    exc, scenario = await run_scenario(80, [], expect_error=OSError)
    assert "no results found" in str(exc)


async def test_cancel(autojump_clock):
    with trio.move_on_after(5) as cancel_scope:
        exc, scenario = await run_scenario(
            80,
            [
                ("1.1.1.1", 10, "success"),
                ("2.2.2.2", 10, "success"),
                ("3.3.3.3", 10, "success"),
                ("4.4.4.4", 10, "success"),
            ],
            expect_error=trio.MultiError,
        )
        # What comes out should be 1 or more Cancelled errors that all belong
        # to this cancel_scope; this is the easiest way to check that
        raise exc
    assert cancel_scope.cancelled_caught

    assert trio.current_time() == 5

    # This should have been called already, but just to make sure, since the
    # exception-handling logic in run_scenario is a bit complicated and the
    # main thing we care about here is that all the sockets were cleaned up.
    scenario.check(succeeded=False)
