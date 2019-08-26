from . base import compare_lists
from baconlang import generate_solutions


def test_basic():
    assert compare_lists(
        generate_solutions('["a"]'),
        [
            [],
            ["a"],
        ],
    )


def test_medium():
    assert compare_lists(
        generate_solutions('["a", "b"]'),
        [
            [],
            ["a"],
            ["b"],
        ],
    )

    assert compare_lists(
        generate_solutions('[["a", "b"]]'),
        [
            [],
            ["a", "b"],
        ],
    )


def test_advanced():
    assert compare_lists(
        generate_solutions(
            '["a", [["b", ["c", [["d", "e"]], "d"] ]] ]'
        ),
        [
            [],
            ["a"],
            ["b", "c"],
            ["b", "d", "e"],
            ["b", "e"],
        ],
    )

