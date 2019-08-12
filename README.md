# [baclang](https://github.com/baclang/python) - Bracket annotated constraint interpreter

---

BAClang is a logical programming language dedicated to evaluating constraint based expressions using only strings and square brackets. This package allows for:
- Parsing of valid BACs using either symbol maps or evaluators
- Generation of all possible symbol maps for a given constraint
- Generation of all satisfactory symbol maps for a given constraint

---

### baclang.interpret(expression, symbol_map=False, evaluator=False)
Return an array representing the result of a BAC expression given either a symbol map or evaluator. If both a symbol map or evaluator is passed in, a `BACLangEvaluationError` is raised.

`symbol map` is a dictionary used to map strings in the BAC expression to a value. This determines which strings evaluate as truthy in the BAC. If strings within the BAC are not found in the object, the string will default to falsey during evaluation.

```
>>> from baclang import interpret
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
>>> from baclang import interpret
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

### baclang.generate_symbol_maps(expression)
Returns a list of __baclang.SymbolMap__ representing all possible symbol map inputs for a given expression.

```
>>> from baclang import generate_symbol_maps
>>> generate_symbol_maps('["a"]')
[{'symbol_map': {'a': 0}, 'evaluation': []}, {'symbol_map': {'a': 1}, 'evaluation': ['a']}]
>>> generate_symbol_maps('["a", "b"]')
[{'symbol_map': {'b': 0, 'a': 0}, 'evaluation': []}, {'symbol_map': {'b': 0, 'a': 1}, 'evaluation': ['a']}, {'symbol_map': {'b': 1, 'a': 0}, 'evaluation': ['b']}, {'symbol_map': {'b': 1, 'a': 1}, 'evaluation': ['a']}]
```

---

### baclang.generate_solutions(expression)
Returns a list of lists representing all solutions for a given expression.

```
>>> from baclang import generate_symbol_maps
>>> generate_solutions('["a"]')
[[], ['a']]
>>> generate_solutions('["a", "b"]')
[[], ['a'], ['b']]
>>> generate_solutions('[["a", "b"]]')
[[], ['a', 'b']]
```

---

## class baclang.SymbolMap(expression, symbol_map)
Return an instance of `baclang.SymbolMap` that contains the provided symbol map as well as the result of evaluating the symbol map against a BAC expression.

#### symbol_map
The symbol_map provided upon instantiation

#### evaluation
The result of the evaluated BAC expression given the provided symbol map

```
>>> from baclang.classes import SymbolMap
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

