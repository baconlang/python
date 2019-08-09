from baclang.parse import parse
from baclang.baclang_evaluation_error import BACLangEvaluationError


def interpret(
    expression,
    symbol_map=False,
    evaluator=False,
):
    if not symbol_map and not evaluator:
        raise BACLangEvaluationError()

    if symbol_map and evaluator:
        raise BACLangEvaluationError()

    parsed_expression = parse(expression)
    queue = []
    for symbol in parsed_expression:
        if symbol == "[" or symbol == "]":
            queue.append(symbol)
            continue

        if (symbol_map and symbol_map.get(symbol))\
                or (evaluator and evaluator([symbol])):
            queue.append([symbol])
            continue

        queue.append([])

    s_clusters = []
    idx = 0

    while idx < len(queue):
        if queue[idx] == "]":
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
                    and queue[idx+1] == "]"\
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
                    if not len(element):
                        new_element = []
                        break

                    new_element += element

                # If evaluator exists
                # and new_element is not empty
                # and evaluator returns False
                # invalidate new element
                if evaluator\
                        and len(new_element)\
                        and not evaluator(new_element):
                    new_element = []

                queue[eval_start:idx+1] = [new_element]

            idx -= idx - eval_start

            # Clear empty symbol clusters
            if s_clusters[-1][0] is 0:
                del s_clusters[-1]

            continue

        if queue[idx] == "[":
            # Extend the current cluster
            if idx > 0 and queue[idx - 1] == "[":
                s_clusters[-1][0] += 1

            # The start of a new cluster
            else:
                s_clusters.append([1,idx])
            idx += 1
            continue

        if idx\
                and not queue[idx] == "["\
                and not queue[idx] == "]"\
                and queue[idx-1] == "["\
                and queue[idx+1] == "]":
            del queue[idx-1]
            del queue[idx]
            idx -= 1
            continue

        idx += 1

    return [
        symbol for symbol in queue[0]
    ]


