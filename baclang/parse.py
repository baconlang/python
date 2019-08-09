from baclang.baclang_syntax_error import BACLangSyntaxError


def parse(raw):
    symbols = [
        symbol.strip()
        for symbol in raw.replace("[", "[,").replace("]", ",]").split(",")
    ]

    for idx, symbol in enumerate(symbols):
        if symbol is "[" or symbol is "]":
            continue

        if len(symbol) and symbol[0] is '"' and symbol[-1] is '"':
            symbols[idx] = symbol[1:-1]

        else:
            # Only valid strings are legal symbols
            raise BACLangSyntaxError(symbol)

    return symbols
