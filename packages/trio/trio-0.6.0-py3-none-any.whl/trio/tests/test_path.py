import os
import pathlib

import pytest

import trio
from trio._path import AsyncAutoWrapperType as Type
from trio._util import fspath
from trio._file_io import AsyncIOWrapper


@pytest.fixture
def path(tmpdir):
    p = str(tmpdir.join('test'))
    return trio.Path(p)


def method_pair(path, method_name):
    path = pathlib.Path(path)
    async_path = trio.Path(path)
    return getattr(path, method_name), getattr(async_path, method_name)


async def test_open_is_async_context_manager(path):
    async with await path.open('w') as f:
        assert isinstance(f, AsyncIOWrapper)

    assert f.closed


async def test_magic():
    path = trio.Path('test')

    assert str(path) == 'test'
    assert bytes(path) == b'test'


cls_pairs = [
    (trio.Path, pathlib.Path),
    (pathlib.Path, trio.Path),
    (trio.Path, trio.Path)
]


@pytest.mark.parametrize('cls_a,cls_b', cls_pairs)
async def test_cmp_magic(cls_a, cls_b):
    a, b = cls_a(''), cls_b('')
    assert a == b
    assert not a != b

    a, b = cls_a('a'), cls_b('b')
    assert a < b
    assert b > a

    # this is intentionally testing equivalence with none, due to the
    # other=sentinel logic in _forward_magic
    assert not a == None
    assert not b == None


# upstream python3.5 bug: we should also test (pathlib.Path, trio.Path), but
# __*div__ does not properly raise NotImplementedError like the other comparison
# magic, so trio.Path's implementation does not get dispatched
cls_pairs = [
    (trio.Path, pathlib.Path),
    (trio.Path, trio.Path),
    (trio.Path, str),
    (str, trio.Path)
]


@pytest.mark.parametrize('cls_a,cls_b', cls_pairs)
async def test_div_magic(cls_a, cls_b):
    a, b = cls_a('a'), cls_b('b')

    result = a / b
    assert isinstance(result, trio.Path)
    assert str(result) == os.path.join('a', 'b')


async def test_forwarded_properties(path):
    # use `name` as a representative of forwarded properties

    assert 'name' in dir(path)
    assert path.name == 'test'


async def test_async_method_signature(path):
    # use `resolve` as a representative of wrapped methods

    assert path.resolve.__name__ == 'resolve'
    assert path.resolve.__qualname__ == 'Path.resolve'

    assert 'pathlib.Path.resolve' in path.resolve.__doc__


@pytest.mark.parametrize('method_name', ['is_dir', 'is_file'])
async def test_compare_async_stat_methods(method_name):

    method, async_method = method_pair('.', method_name)

    result = method()
    async_result = await async_method()

    assert result == async_result


async def test_invalid_name_not_wrapped(path):
    with pytest.raises(AttributeError):
        getattr(path, 'invalid_fake_attr')


@pytest.mark.parametrize('method_name', ['absolute', 'resolve'])
async def test_async_methods_rewrap(method_name):

    method, async_method = method_pair('.', method_name)

    result = method()
    async_result = await async_method()

    assert isinstance(async_result, trio.Path)
    assert str(result) == str(async_result)


async def test_forward_methods_rewrap(path, tmpdir):
    with_name = path.with_name('foo')
    with_suffix = path.with_suffix('.py')

    assert isinstance(with_name, trio.Path)
    assert with_name == tmpdir.join('foo')
    assert isinstance(with_suffix, trio.Path)
    assert with_suffix == tmpdir.join('test.py')


async def test_forward_properties_rewrap(path):
    assert isinstance(path.parent, trio.Path)


async def test_forward_methods_without_rewrap(path, tmpdir):
    path = await path.parent.resolve()

    assert path.as_uri().startswith('file:///')


async def test_repr():
    path = trio.Path('.')

    assert repr(path) == "trio.Path('.')"


class MockWrapped:
    unsupported = 'unsupported'
    _private = 'private'


class MockWrapper:
    _forwards = MockWrapped
    _wraps = MockWrapped


async def test_type_forwards_unsupported():
    with pytest.raises(TypeError):
        Type.generate_forwards(MockWrapper, {})


async def test_type_wraps_unsupported():
    with pytest.raises(TypeError):
        Type.generate_wraps(MockWrapper, {})


async def test_type_forwards_private():
    Type.generate_forwards(MockWrapper, {'unsupported': None})

    assert not hasattr(MockWrapper, '_private')


async def test_type_wraps_private():
    Type.generate_wraps(MockWrapper, {'unsupported': None})

    assert not hasattr(MockWrapper, '_private')


@pytest.mark.parametrize('meth', [trio.Path.__init__, trio.Path.joinpath])
async def test_path_wraps_path(path, meth):
    wrapped = await path.absolute()
    result = meth(path, wrapped)
    if result is None:
        result = path

    assert wrapped == result


async def test_path_nonpath():
    with pytest.raises(TypeError):
        trio.Path(1)


async def test_open_file_can_open_path(path):
    async with await trio.open_file(path, 'w') as f:
        assert f.name == fspath(path)


async def test_iterdir(path):
    # Populate a directory
    await path.mkdir()
    await (path / 'foo').mkdir()
    await (path / 'bar.txt').write_bytes(b'')

    entries = set()
    for entry in await path.iterdir():
        assert isinstance(entry, trio.Path)
        entries.add(entry.name)

    assert entries == {'bar.txt', 'foo'}
