#   This example uses expressions to describe grocery lists
#
#   The output of an expression given static or dynamic data is the
#   solution given the context
#

from baconlang import (
    interpret,
)

# Our data (symbol maps)

def get_food_leopard_data():
    return dict(
        tomato=5,
        lemon=6,
        lime=2,
        hotdog_bun=4,
        hotdog=2,
        hamburger_bun=6,
        hamburger=3,
        open=False,
    )


def get_harry_peters_data():
    return dict(
        tomato=2,
        lemon=0,
        lime=4,
        hotdog_bun=0,
        hotdog=5,
        hamburger_bun=2,
        hamburger=6,
        open=True,
    )


# Our constraints (expression)

# We need a tomato AND a lemon AND a hotdog_bun AND a hotdog
expression_a = '[["tomato", "lemon", "hotdog_bun", "hotdog"]]'


# We need a tomato, and a lemon OR lime OR nothing.
expression_b = '[["tomato", ["lemon", "lime", "null"]]]'


# We need 2 tomatos AND 1 lemon AND ((1 hotdog_bun AND 1 hotdog) OR (1 hamburger_bun AND 1 hamburger))
expression_c = '[["tomato", "tomato", "lime", [[["hotdog_bun", "hotdog"]], [["hamburger_bun", "hamburger"]]]]]'


# If harry_peters is open, try to get 1 tomato AND 1 lemon AND 1 lime AND 1 hotdog_bun and 1 hotdog
# OR go to food_leopard and get 1 tomato AND 1 lime AND 1 hamburger_bun AND 1 hamburger
expression_d = '[ [["harry_peters", "tomato", "lemon", "lime", "hotdog_bun", "hotdog"]], [["food_leopard", "tomato", "lime", "hamburger_bun", "hamburger"]] ]'


# Solutions to our constraints given static data

result_a = interpret(
    expression_a,
    symbol_map=get_food_leopard_data(),
)
print(result_a)


result_b = interpret(
    expression_b,
    symbol_map=get_harry_peters_data(),
)
print(result_b)


result_c = interpret(
    expression_c,
    symbol_map=get_harry_peters_data(),
)
print(result_c)


# Solutions to our constraints given a more accurate model
        
def evaluator_a(elements):
    # Modeling the store "harry_peters" being closed
    if 'harry_peters' in elements:
        data = get_harry_peters_data()

    elif 'food_leopard' in elements:
        data = get_food_leopard_data()

    # We only want to evaluate statements that we have data for
    # i.e. one of the two stores
    else:
        return True

    for element in elements:
        # Acounting for the "food_leopard" symbol
        if element == 'food_leopard' or element == 'harry_peters':
            continue

        # Check for the item being in stock
        if data.get(element):
            # Reduce stock and continue evaluation of the given expression
            data[element] -= 1
            continue

        # Not in stock, expression is falsey
        else:
            return False

    # If all symbols were evaluated correctly, we return True
    return True

result_e_a = interpret(
    expression_d,
    evaluator=evaluator_a,
)
print(result_e_a)


def evaluator_b(elements):
    # Modeling the store "harry_peters" being closed
    if 'harry_peters' in elements:
        return False

    data = get_food_leopard_data()

    for element in elements:
        # Acounting for the "food_leopard" symbol
        if element == 'food_leopard':
            continue

        # Check for the item being in stock
        if data.get(element):
            # Reduce stock and continue evaluation of the given expression
            data[element] -= 1
            continue

        # Not in stock, expression is falsey
        else:
            return False

    # If all symbols were evaluated correctly, we return True
    return True


result_e_b = interpret(
    expression_b,
    evaluator=evaluator_b,
)
print(result_e_b)

