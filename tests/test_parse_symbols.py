from baclang import parse_symbols
from . base import compare_lists


def test_size_1():
    assert compare_lists(
        parse_symbols('["a"]'),
        ['a'],
    )


def test_size_2():
    assert compare_lists(
        parse_symbols('["a", "b"]'),
        ['a', 'b'],
    )


def test_size_3():
    assert compare_lists(
        parse_symbols('["a", "b", "c"]'),
        ['a', 'b', 'c'],
    )


def test_size_4():
    assert compare_lists(
        parse_symbols('["a", "b", "c", "d"]'),
        ['a', 'b', 'c', 'd'],
    )
