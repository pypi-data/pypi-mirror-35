import pytest
from dig.utils.data_types import *

@pytest.mark.parametrize('str, result', [
    ("hello", True),
    ({"1":"2"}, False),
    ('\u0394', True),
    (["a", "b"], False)
])
def test_is_str(str, result):
    assert is_str(str) == result


@pytest.mark.parametrize('str, result', [
    ("hello", False),
    ({"1":"2"}, False),
    ('\u0394', False),
    (["a", "b"], True),
    (("a", "b"), True),
])
def test_is_list(str, result):
    assert is_list(str) == result


@pytest.mark.parametrize('str1, str2, result', [
    ("hello", "hello", 0),
    ("String method tutorial", "compareTo method example", -1),
    ("String method tutorial", "String method tutorial", 0),
    ("compareTo method example", "String method tutorial", 1)
])
def test_str_compare(str1, str2, result):
    assert str_compare(str1, str2) == result


@pytest.mark.parametrize('t, result', [
    ("hello", ["hello"]),
    ({"1":"2"}, [{"1":"2"}]),
    (["a", "b"], ["a", "b"])
])
def test_to_list(t, result):
    assert to_list(t) == result