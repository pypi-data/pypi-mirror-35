import io
import tempfile

import pytest
from unittest import mock
from unittest.mock import sentinel

import trio
from trio import _core
from trio._util import fspath
from trio._file_io import AsyncIOWrapper, _FILE_SYNC_ATTRS, _FILE_ASYNC_METHODS


@pytest.fixture
def path(tmpdir):
    return fspath(tmpdir.join('test'))


@pytest.fixture
def wrapped():
    return mock.Mock(spec_set=io.StringIO)


@pytest.fixture
def async_file(wrapped):
    return trio.wrap_file(wrapped)


def test_wrap_invalid():
    with pytest.raises(TypeError):
        trio.wrap_file(str())


def test_wrap_non_iobase():
    class FakeFile:
        def close(self):  # pragma: no cover
            pass

        def write(self):  # pragma: no cover
            pass

    wrapped = FakeFile()
    assert not isinstance(wrapped, io.IOBase)

    async_file = trio.wrap_file(wrapped)
    assert isinstance(async_file, AsyncIOWrapper)

    del FakeFile.write

    with pytest.raises(TypeError):
        trio.wrap_file(FakeFile())


def test_wrapped_property(async_file, wrapped):
    assert async_file.wrapped is wrapped


def test_dir_matches_wrapped(async_file, wrapped):
    attrs = _FILE_SYNC_ATTRS.union(_FILE_ASYNC_METHODS)

    # all supported attrs in wrapped should be available in async_file
    assert all(
        attr in dir(async_file) for attr in attrs if attr in dir(wrapped)
    )
    # all supported attrs not in wrapped should not be available in async_file
    assert not any(
        attr in dir(async_file) for attr in attrs if attr not in dir(wrapped)
    )


def test_unsupported_not_forwarded():
    class FakeFile(io.RawIOBase):
        def unsupported_attr(self):  # pragma: no cover
            pass

    async_file = trio.wrap_file(FakeFile())

    assert hasattr(async_file.wrapped, 'unsupported_attr')

    with pytest.raises(AttributeError):
        getattr(async_file, 'unsupported_attr')


def test_sync_attrs_forwarded(async_file, wrapped):
    for attr_name in _FILE_SYNC_ATTRS:
        if attr_name not in dir(async_file):
            continue

        assert getattr(async_file, attr_name) is getattr(wrapped, attr_name)


def test_sync_attrs_match_wrapper(async_file, wrapped):
    for attr_name in _FILE_SYNC_ATTRS:
        if attr_name in dir(async_file):
            continue

        with pytest.raises(AttributeError):
            getattr(async_file, attr_name)

        with pytest.raises(AttributeError):
            getattr(wrapped, attr_name)


def test_async_methods_generated_once(async_file):
    for meth_name in _FILE_ASYNC_METHODS:
        if meth_name not in dir(async_file):
            continue

        assert getattr(async_file, meth_name) is getattr(async_file, meth_name)


def test_async_methods_signature(async_file):
    # use read as a representative of all async methods
    assert async_file.read.__name__ == 'read'
    assert async_file.read.__qualname__ == 'AsyncIOWrapper.read'

    assert 'io.StringIO.read' in async_file.read.__doc__


async def test_async_methods_wrap(async_file, wrapped):
    for meth_name in _FILE_ASYNC_METHODS:
        if meth_name not in dir(async_file):
            continue

        meth = getattr(async_file, meth_name)
        wrapped_meth = getattr(wrapped, meth_name)

        value = await meth(sentinel.argument, keyword=sentinel.keyword)

        wrapped_meth.assert_called_once_with(
            sentinel.argument, keyword=sentinel.keyword
        )
        assert value == wrapped_meth()

        wrapped.reset_mock()


async def test_async_methods_match_wrapper(async_file, wrapped):
    for meth_name in _FILE_ASYNC_METHODS:
        if meth_name in dir(async_file):
            continue

        with pytest.raises(AttributeError):
            getattr(async_file, meth_name)

        with pytest.raises(AttributeError):
            getattr(wrapped, meth_name)


async def test_open(path):
    f = await trio.open_file(path, 'w')

    assert isinstance(f, AsyncIOWrapper)

    await f.aclose()


async def test_open_context_manager(path):
    async with await trio.open_file(path, 'w') as f:
        assert isinstance(f, AsyncIOWrapper)
        assert not f.closed

    assert f.closed


async def test_async_iter():
    async_file = trio.wrap_file(io.StringIO('test\nfoo\nbar'))
    expected = list(async_file.wrapped)
    result = []
    async_file.wrapped.seek(0)

    async for line in async_file:
        result.append(line)

    assert result == expected


async def test_aclose_cancelled(path):
    with _core.open_cancel_scope() as cscope:
        f = await trio.open_file(path, 'w')
        cscope.cancel()

        with pytest.raises(_core.Cancelled):
            await f.write('a')

        with pytest.raises(_core.Cancelled):
            await f.aclose()

    assert f.closed


async def test_detach_rewraps_asynciobase():
    raw = io.BytesIO()
    buffered = io.BufferedReader(raw)

    async_file = trio.wrap_file(buffered)

    detached = await async_file.detach()

    assert isinstance(detached, AsyncIOWrapper)
    assert detached.wrapped is raw
