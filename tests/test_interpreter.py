from baclang import interpreter

from . base import symgem

a='a';b='b';c='c'

def check(exp, val, binary):
    sym = symgem(binary)
    assert interpreter(exp, sym) == val

def checkswbin(binary, cases):
    for case in cases:
        check(*case, binary)

def checkswexp(exp, cases):
    for case in cases:
        check(exp, *case[::-1])

def nuke(exp):
    parsed_exp = exp.replace('[','')
    parsed_exp = parsed_exp.replace(']','')
    parsed_exp = parsed_exp.replace(' ','')
    symbol_len = len(set(parsed_exp.split(',')))
    bin_list = []
    for test in range(int(f'0b{"1"*symbol_len}',2)+1):
        binary = bin(test)
        binary += '0'*(symbol_len-len(binary)+2)
        if not binary in bin_list:
            interpreter(exp, symgem(binary))
            bin_list.append(binary)

def test_single_condition():
    checkswbin(
        '0b0',
        [
            ['["a"]', []],
            ['[["a"]]', []],
            ['[[["a"]]]', []],
        ],
    )

    checkswbin(
        '0b1',
        [
            ['["a"]', [a]],
            ['[["a"]]', [a]],
            ['[[["a"]]]', [a]],
        ],
    )

def test_double_condition():
    checkswexp(
        '["a", "b"]',
        [
            ['0b00', []],
            ['0b10', [a]],
            ['0b01', [b]],
            ['0b11', [a]],
        ],
    )

    checkswexp(
        '[["a", "b"]]',
        [
            ['0b00', []],
            ['0b10', []],
            ['0b01', []],
            ['0b11', [a,b]],
        ],
    )

def test_triple_condition():
    identical_cases_1 = [
        ['0b000', []],
        ['0b100', [a]],
        ['0b010', [b]],
        ['0b110', [a]],
        ['0b001', [c]],
        ['0b101', [a]],
        ['0b011', [b]],
        ['0b111', [a]],
    ]

    checkswexp('["a", "b", "c"]', identical_cases_1)
    checkswexp('[["a", "b"], "c"]', identical_cases_1)
    checkswexp('["a", ["b", "c"]]', identical_cases_1)

    checkswexp(
        '[[["a", "b"]], "c"]',
        [
            ['0b000', []],
            ['0b100', []],
            ['0b010', []],
            ['0b110', [a,b]],
            ['0b001', [c]],
            ['0b101', [c]],
            ['0b011', [c]],
            ['0b111', [a,b]],
        ],
    )
    checkswexp(
        '["a", [["b", "c"]]]',
        [
            ['0b000', []],
            ['0b100', [a]],
            ['0b010', []],
            ['0b110', [a]],
            ['0b001', []],
            ['0b101', [a]],
            ['0b011', [b,c]],
            ['0b111', [a]],
        ],
    )

    identical_cases_2 = [
        ['0b000', []],
        ['0b100', []],
        ['0b010', []],
        ['0b110', []],
        ['0b001', []],
        ['0b101', []],
        ['0b011', []],
        ['0b111', [a,b,c]],
    ]

    checkswexp( '[["a", "b", "c"]]', identical_cases_2)
    checkswexp('[[[["a", "b"]], "c"]]', identical_cases_2)
    checkswexp('[["a", [["b", "c"]]]]', identical_cases_2)   

    checkswexp(
        '[[["a", "b"], "c"]]',
        [
            ['0b000', []],
            ['0b100', []],
            ['0b010', []],
            ['0b110', []],
            ['0b001', []],
            ['0b101', [a,c]],
            ['0b011', [b,c]],
            ['0b111', [a,c]],
        ],
    )
    checkswexp(
        '[["a", ["b", "c"]]]',
        [
            ['0b000', []],
            ['0b100', []],
            ['0b010', []],
            ['0b110', [a,b]],
            ['0b001', []],
            ['0b101', [a,c]],
            ['0b011', []],
            ['0b111', [a,b]],
        ],
    )

def test_nuke():
    nuke('[["a", ["b", [[["c", "d"], "e"]]]]]')

