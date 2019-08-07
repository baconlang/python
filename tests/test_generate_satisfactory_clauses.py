from . base import compare_lists
from baclang import generate_satisfactory_clauses


def test_basic():
    assert compare_lists(
        generate_satisfactory_clauses('["a"]'),
        [
            [],
            ["a"],
        ],
    )


def test_medium():
    assert compare_lists(
        generate_satisfactory_clauses('["a", "b"]'),
        [
            [],
            ["a"],
            ["b"],
        ],
    )

    assert compare_lists(
        generate_satisfactory_clauses('[["a", "b"]]'),
        [
            [],
            ["a", "b"],
        ],
    )


def test_advanced():
    assert compare_lists(
        generate_satisfactory_clauses(
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

