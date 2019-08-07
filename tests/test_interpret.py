from baclang import (
    interpret,
    generate_symbol_maps,
)
from . base import (
    sym_gen,
    compare_lists,
)

a = 'a'
b = 'b'
c = 'c'


def assert_symbol_map(exp, *args):
    for case in args:
        symbol_map = sym_gen(case[0])

        def evaluator(symbols):
            for symbol in symbols:
                if not symbol_map.get(symbol):
                    return False
            return True

        assert compare_lists(
            interpret(exp, evaluator=evaluator),
            case[1],
        )


def assert_evaluator(exp, *args):
    for case in args:
        assert compare_lists(
            interpret(exp, symbol_map=sym_gen(case[0])),
            case[1],
        )


single_scenarios = (
    ('0b0', []),
    ('0b1', [a]),
)

single_expressions = (
    ('["a"]', *single_scenarios),
    ('[["a"]]', *single_scenarios),
    ('[[["a"]]]', *single_scenarios),
)


def test_symbol_map_single_condition():
    for parameter in single_expressions:
        assert_symbol_map(*parameter)


def test_evaluator_single_condition():
    for parameter in single_expressions:
        assert_evaluator(*parameter)


double_expressions = (
    (
        '["a", "b"]',
        ('0b00', []),
        ('0b10', [a]),
        ('0b01', [b]),
        ('0b11', [a]),
    ),
    (
        '[["a", "b"]]',
        ('0b00', []),
        ('0b10', []),
        ('0b01', []),
        ('0b11', [a,b]),
    ),
)


def test_symbol_map_double_condition():
    for parameter in double_expressions:
        assert_symbol_map(*parameter)


def test_evaluator_double_condition():
    for parameter in double_expressions:
        assert_evaluator(*parameter)


triple_scenarios_1 = (
    ('0b000', []),
    ('0b100', [a]),
    ('0b010', [b]),
    ('0b110', [a]),
    ('0b001', [c]),
    ('0b101', [a]),
    ('0b011', [b]),
    ('0b111', [a]),
)

triple_scenarios_2 = (
    ('0b000', []),
    ('0b100', []),
    ('0b010', []),
    ('0b110', []),
    ('0b001', []),
    ('0b101', []),
    ('0b011', []),
    ('0b111', [a,b,c]),
)

triple_expressions = (
    ('["a", "b", "c"]', *triple_scenarios_1),
    ('[["a", "b"], "c"]', *triple_scenarios_1),
    ('["a", ["b", "c"]]', *triple_scenarios_1),
    (
        '[[["a", "b"]], "c"]',
        ('0b000', []),
        ('0b100', []),
        ('0b010', []),
        ('0b110', [a,b]),
        ('0b001', [c]),
        ('0b101', [c]),
        ('0b011', [c]),
        ('0b111', [a,b]),
    ),
    (
        '["a", [["b", "c"]]]',
        ('0b000', []),
        ('0b100', [a]),
        ('0b010', []),
        ('0b110', [a]),
        ('0b001', []),
        ('0b101', [a]),
        ('0b011', [b,c]),
        ('0b111', [a]),
    ),
    ('[["a", "b", "c"]]', *triple_scenarios_2),
    ('[[[["a", "b"]], "c"]]', *triple_scenarios_2),
    ('[["a", [["b", "c"]]]]', *triple_scenarios_2),
    (
        '[[["a", "b"], "c"]]',
        ('0b000', []),
        ('0b100', []),
        ('0b010', []),
        ('0b110', []),
        ('0b001', []),
        ('0b101', [a,c]),
        ('0b011', [b,c]),
        ('0b111', [a,c]),
    ),
    (
        '[["a", ["b", "c"]]]',
        ('0b000', []),
        ('0b100', []),
        ('0b010', []),
        ('0b110', [a,b]),
        ('0b001', []),
        ('0b101', [a,c]),
        ('0b011', []),
        ('0b111', [a,b]),
    ),
)


def test_symbol_map_triple_condition():
    for parameter in triple_expressions:
        assert_symbol_map(*parameter)


def test_evaluator_triple_condition():
    for parameter in triple_expressions:
        assert_evaluator(*parameter)


def test_nuke():
    assert generate_symbol_maps('[["a", ["b", [[["c", "d"], "e"]]]]]')


def assert_called_with(expression, *args):
    called_with = []

    def evaluator(symbols):
        called_with.append(symbols)
        for symbol in symbols:
            if symbol == 'False':
                return False
        return True
    interpret(expression, evaluator=evaluator)
    assert called_with == list(args)


def test_evaluator_calls():
    assert_called_with(
        '["a", "b", "c", "d"]',
        ["a"],
        ["b"],
        ["c"],
        ["d"],
    )

    assert_called_with(
        '["a", "False", "c", "d"]',
        ["a"],
        ["False"],
        ["c"],
        ["d"],
    )

    assert_called_with(
        '["a", ["False", "c"], "d"]',
        ["a"],
        ["False"],
        ["c"],
        ["d"],
    )

    assert_called_with(
        '["a", [["b", "c"]], "d"]',
        ["a"],
        ["b"],
        ["c"],
        ["d"],
        ["b", "c"],
    )

    assert_called_with(
        '[["a", [["b", "c"]], "d"]]',
        ["a"],
        ["b"],
        ["c"],
        ["d"],
        ["b", "c"],
        ["a", "b", "c", "d"],
    )

    assert_called_with(
        '[["False", [["b", "c"]], "d"]]',
        ["False"],
        ["b"],
        ["c"],
        ["d"],
        ["b", "c"],
    )

    assert_called_with(
        '[["a", [["False", "c"]], "d"]]',
        ["a"],
        ["False"],
        ["c"],
        ["d"],
    )

