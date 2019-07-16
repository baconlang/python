from . classes import EvaluatedSymbol

def interpreter(
    requirements,
    symbol_map=False,
    evaluator=False,
    preserve_symbol=True,
):
    if not symbol_map and not evaluator:
        raise TypeError('Missing method of evaluation')

    string = requirements.replace("[", "[,")
    string = string.replace("]", ",]")
    queue = []
    for symbol in string.split(","):
        symbol = symbol.strip()
        if symbol is "[" or symbol is "]":
            queue.append(symbol)
            continue

        # Check if symbol is string
        if len(symbol) and symbol[0] is '"' and symbol[-1] is '"':
            symbol = symbol[1:-1]
        else:
            # Only valid strings are legal symbols
            raise SyntaxError(symbol)

        # If AOT compiled
        if symbol_map:
            evaluated_symbol = symbol_map.get(symbol)
            if evaluated_symbol:
                queue.append([
                    preserve_symbol and symbol or evaluated_symbol
                ])
                continue

            queue.append([])
            continue

        queue.append([symbol])

    s_clusters = []
    idx = 0

    while idx < len(queue):
        if queue[idx] is "]":
            # Remove elements and set the index to
            # the element before the first bracket
            s_clusters[-1][0] -= 1
            # Always delete last to first
            del queue[idx]
            del queue[s_clusters[-1][1]]
            idx -= 2
            and_operator = False
            
            # If the current index is not the last
            # And if the next index is a bracket symbol
            # And the last symbol cluster still has space
            if idx < len(queue)-1\
            and queue[idx+1] is "]"\
            and s_clusters[-1][0] > 0:
                # Remove the elements and set the index
                # to the element before the second bracket
                s_clusters[-1][0] -= 1
                # We were immediately behind
                # the last bracket so this is 1
                del queue[idx+1]
                del queue[s_clusters[-1][1]]
                idx -= 1
                and_operator = True

            # Set the start of evaluation to the index
            # of the last symbol cluster plus its size
            eval_start = s_clusters[-1][1] + s_clusters[-1][0]

            # Evaluate current element cluster
            if not and_operator:
                found = False
                # If a valid element is found set the range to that
                for element in queue[eval_start:idx+1]:
                    
                    # if potential unevaluated symbol
                    # and evaluator is true
                    if len(element) == 1\
                    and evaluator\
                    and type(element[0]) is not EvaluatedSymbol:
                        evaluated_symbol = evaluator(element)
                        if evaluated_symbol:
                            if preserve_symbol:
                                element = EvaluatedSymbol(element)
                            else:
                                element = EvaluatedSymbol(
                                    evaluated_symbol,
                                )
                        else:
                            element = []

                    if len(element):
                        queue[eval_start:idx+1] = [element]
                        found = True
                        break

                # If nothing was found, the range should be false
                if not found:
                    queue[eval_start:idx+1] = [[]]

            else:
                new_element = []
                # If no elements in the range are
                # valid set the range to false
                for element in queue[eval_start:idx+1]:
                    if len(element) == 1\
                    and evaluator\
                    and type(element[0]) is not EvaluatedSymbol:
                        evaluated_symbol = evaluator(element)
                        if evaluated_symbol:
                            if preserve_symbol:
                                element = EvaluatedSymbol(element)
                            else:
                                element = EvaluatedSymbol(
                                    evaluated_symbol,
                                )
                        else:
                            element = []

                    if not len(element):
                        new_element = []
                        break

                    new_element += element

                queue[eval_start:idx+1] = [new_element]

            idx -= idx - eval_start

            # Clear empty symbol clusters
            if s_clusters[-1][0] is 0:
                del s_clusters[-1]

            continue

        if queue[idx] is "[":
            # Extend the current cluster
            if idx > 0 and queue[idx - 1] is "[":
                s_clusters[-1][0] += 1

            # The start of a new cluster
            else:
                s_clusters.append([1,idx])
            idx += 1
            continue

        if idx\
        and queue[idx] is not "["\
        and queue[idx] is not "]"\
        and queue[idx-1] is "["\
        and queue[idx+1] is "]":
            del queue[idx-1]
            del queue[idx]
            idx -= 1
            continue

        idx += 1

    return [
        type(symbol) is EvaluatedSymbol and symbol.value or symbol\
        for symbol in queue[0]
    ]


