import cProfile
import pstats
from itertools import repeat

from baconlang import interpret, generate_symbol_maps

N = 500


def profile_all_symbol_maps(exp, cmet):
    diffs = []
    for symbol_map in generate_symbol_maps(exp):
        def evaluator(symbols):
            if len(symbols) == 1:
                return symbol_map.symbol_map.get(symbols[0])

        py_avg = average_total_tt(
            cmet(evaluator),
            N,
        )

        bac_avg = average_total_tt(
            bac_eval(exp, evaluator),
            N,
        )

        diffs.append((
            (bac_avg - py_avg) / py_avg * 100,
            bac_avg * 1000,
            py_avg * 1000,
            symbol_map,
        ))
    return sum([diff[0] for diff in diffs]) / len(diffs)


def total_tt(method):
    pr = cProfile.Profile()
    pr.enable()
    method()
    pr.disable()
    return pstats.Stats(pr).total_tt


def average_total_tt(method, n):
    return sum([total_tt(method) for _ in repeat(None, n)]) / n


def bac_eval(expression, evaluator):
    return lambda : interpret(
        expression,
        evaluator=evaluator,
    )


def bac_map(expression, symbol_map):
    return lambda : interpret(
        expression,
        symbol_map=symbol_map,
    )


def test_a_and_b_and_c():
    avg_diff = profile_all_symbol_maps(
        '[["a", "b", "c"]]',
        lambda evaluator: lambda:\
        evaluator('a')\
        and evaluator('b')\
        and evaluator('c'),
    )

    avg_diff = profile_all_symbol_maps(
        '[["a", ["b", "c"]]]',
        lambda evaluator: lambda:
        evaluator('a') and (evaluator('b') or evaluator('c')),
    )

