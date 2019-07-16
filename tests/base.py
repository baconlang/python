import collections
import string

field_names = list(string.ascii_lowercase)
defaults = [0] * len(field_names)
SymbolMap = collections.namedtuple(
    'SymbolMap',
    field_names,
    defaults=defaults,
)

def symgem(ohe):
    symbol_map = {}
    field_names = list(string.ascii_lowercase)
    for idx, enc in enumerate(ohe[2:]):
        symbol_map[field_names[idx]] = int(enc)
    return symbol_map
