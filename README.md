# [baconlang](https://github.com/baconlang/python) - Bracket Annotated CONstraint interpreter

---

BACONLang is a logical programming language dedicated to evaluating constraint based expressions using only strings and square brackets. This package allows for:
- Parsing of valid BACON expressions using either symbol maps or evaluators
- Generation of all possible symbol maps for a given BACON expression
- Generation of all solutions for a given BACON expression

---

### baconlang.interpret(expression, symbol_map=False, evaluator=False)
Return an array representing the result of a BACON expression given either a symbol map or evaluator. If both a symbol map or evaluator is passed in, a `BACONLangEvaluationError` is raised.

`symbol map` is a dictionary used to map strings in the BACON expression to a value. This determines which strings evaluate as truthy in the BACON expression. If strings within the BACON expression are not found in the object, the string will default to falsey during evaluation.

```
>>> from baconlang import interpret
>>> expression = '[["a", "b", "c"]]'
>>> symbol_map = dict(
>>>     a=True,
>>>     b=True,
>>>     c=True,
>>> )
>>> interpret(expression, symbol_map=symbol_map)
['a', 'b', 'c']
>>> symbol_map['a'] = False
>>> interpret(expression, symbol_map=symbol_map)
[]
>>> expression = '["a", "b", "c"]'
>>> interpret(expression, symbol_map=symbol_map)
['b']
```

`evaluator` is a method that evaluates sub-expressions as necessary during interpretation. When the interpreter needs to evaluate a collective group of strings, it calls `evaluator` with a list containing said strings. The return value of `evaluator` determines if the group of strings evaluates to truthy or falsey.

```
>>> from baconlang import interpret
>>> expression = '["a", "b", "c"]'
>>> def evaluator(symbols):
>>>     for symbol in symbols:
>>>         if symbol == 'c':
>>>             continue
>>>         return False
>>>     return True
>>> interpret(expression, evaluator=evaluator)
['c']
>>> expression = '[["a", "b", "c"]]
>>> interpret(expression, evaluator=evaluator)
[]
>>> def alternate_evaluator(symbols):
>>>     for symbol in symbols:
>>>         if symbol == 'a':
>>>             continue
>>>         if symbol == 'b':
>>>             continue
>>>         if symbol == 'c':
>>>             continue
>>>         return False
>>>     return True
>>> interpret(expression, evaluator=alternate_evaluator)
['a', 'b', 'c']
```

---

### baconlang.generate_symbol_maps(expression)
Returns a list of __baconlang.SymbolMap__ representing all possible symbol map inputs for a given expression.

```
>>> from baconlang import generate_symbol_maps
>>> generate_symbol_maps('["a"]')
[{'symbol_map': {'a': 0}, 'evaluation': []}, {'symbol_map': {'a': 1}, 'evaluation': ['a']}]
>>> generate_symbol_maps('["a", "b"]')
[{'symbol_map': {'b': 0, 'a': 0}, 'evaluation': []}, {'symbol_map': {'b': 0, 'a': 1}, 'evaluation': ['a']}, {'symbol_map': {'b': 1, 'a': 0}, 'evaluation': ['b']}, {'symbol_map': {'b': 1, 'a': 1}, 'evaluation': ['a']}]
```

---

### baconlang.generate_solutions(expression)
Returns a list of lists representing all solutions for a given expression.

```
>>> from baconlang import generate_symbol_maps
>>> generate_solutions('["a"]')
[[], ['a']]
>>> generate_solutions('["a", "b"]')
[[], ['a'], ['b']]
>>> generate_solutions('[["a", "b"]]')
[[], ['a', 'b']]
```

---

## class baconlang.SymbolMap(expression, symbol_map)
Return an instance of `baconlang.SymbolMap` that contains the provided symbol map as well as the result of evaluating the symbol map against a BACON expression.

#### symbol_map
The symbol_map provided upon instantiation

#### evaluation
The result of the evaluated BACON expression given the provided symbol map

```
>>> from baconlang.classes import SymbolMap
>>> expression = '["a", "b", "c"]'
>>> raw_symbol_map = dict(
>>>     a=False,
>>>     b=True,
>>>     c=True,
>>> )
>>> symbol_map = SymbolMap('["a", "b", "c"]', )
>>> symbol_map
{'symbol_map': {'a': False, 'b': True, 'c': True}, 'evaluation': ['b']}
>>> symbol_map.symbol_map
{'a': False, 'b': True, 'c': True}
>>> symbol_map.evaluation
['b']
```

