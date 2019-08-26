from baconlang import interpret
groceries = '[ [["food_lion", "pasta", "lettuce", "soap", [ [["ham_buns", "hamburgers"]], [["hot_buns", "hotdogs"]] ] ]], [["harris_teeter", "potatos", "potatos"]]]'


def evaluator(symbols):
    available = dict(
        pasta=2,
        lettuce=2,
        soap=2,
        ham_buns=2,
        hamburgers=2,
        hot_buns=2,
        hotdogs=2,
        potatos=2,
    )
    
    for symbol in symbols:
        if symbol == "food_lion":
            return False

        if symbol == "harris_teeter":
            continue

        if available.get(symbol):
            available[symbol] -= 1
            continue
        else:
            return False

    return True


def test_example():
    result = interpret(groceries, evaluator=evaluator)
    print(result)

