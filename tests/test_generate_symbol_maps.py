from baclang import generate_symbol_maps, SymbolMap


def test_basic():
    symbol_maps = generate_symbol_maps('["a"]')
    assert len(symbol_maps) == 2
    for symbol_map in symbol_maps:
        assert type(symbol_map) is SymbolMap


def test_medium():
    symbol_maps = generate_symbol_maps('[["a", "b"], [["c", "a"]], "d"]')
    assert len(symbol_maps) == 2**4
    for symbol_map in symbol_maps:
        assert type(symbol_map) is SymbolMap


def test_advanced():
    symbol_maps = generate_symbol_maps(
        '[["a", "b"], [["c", "d"]], "e", ["f", [["g", "h", "i"]]]]'
    )
    assert len(symbol_maps) == 2**9
    for symbol_map in symbol_maps:
        assert type(symbol_map) is SymbolMap
