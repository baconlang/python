from baclang.interpret import interpret


class SymbolMap:
    def __init__(self, expression, symbol_map):
        self.symbol_map = symbol_map
        self.evaluation = interpret(
            expression,
            symbol_map=self.symbol_map,
        )

    def __repr__(self):
        return str({
            'symbol_map': self.symbol_map,
            'evaluation': self.evaluation,
        })

