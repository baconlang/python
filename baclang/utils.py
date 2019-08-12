from baclang.parse import parse
from baclang.symbol_map import SymbolMap


def parse_symbols(expression):
    parsed = parse(expression)
    return [
        symbol for symbol in set(parsed)
        if not symbol == '[' and not symbol == ']'
    ]


def generate_symbol_maps(expression):
    symbols = parse_symbols(expression)
    return [
        SymbolMap(expression, symbol_map) for symbol_map in (
            {
                symbols[idx]:int(bit)
                for idx, bit in enumerate(
                    format(clause, f"0{len(symbols)}b")
                )
            } for clause in range(2**len(symbols))
        )
    ]


def generate_solutions(expression):
    return [list(evaluation) for evaluation in set([
        tuple(symbol.evaluation)
        for symbol in generate_symbol_maps(expression)
    ])]
