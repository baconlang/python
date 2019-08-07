import string

field_names = list(string.ascii_lowercase)
defaults = [0] * len(field_names)


def sym_gen(binary):
    return {
        string.ascii_lowercase[idx]:int(bit)
        for idx, bit in enumerate(binary[2:])
    }


def compare_lists(*args):
    evaluation = True
    for idx in range(len(args)-2):
        evaluation = evaluation\
            and args[idx].sort() == args[idx+1].sort()
    return evaluation
