

def get_word_plus_reverse_as_list(word):
    w1 = list(word)
    w2 = list(word)
    w2.reverse()
    return w1, w2


def check_across(puzzle, word, verbose = False):
    result = 0
    w1, w2 = get_word_plus_reverse_as_list(word)

    for i in range(len(puzzle[0])):
        for j in range(len(puzzle)):
            if w1 == puzzle[j][i:i+4] or w2 == puzzle[j][i:i+4]: 
                result = result + 1
                if verbose: print(f"line:{j}, column:{i} - {puzzle[j][i:i+4]}")
    return result


def check_down(puzzle, word, verbose = False):
    result = 0
    w1, w2 = get_word_plus_reverse_as_list(word)

    for i in range(len(puzzle[0])):
        for j in range(len(puzzle)):
            if j + len(w1) <= len(puzzle):
                word_down = [ puzzle[j+idx][i] for idx in range(len(w1)) ]

                if w1 == word_down or w2 == word_down: 
                    result = result + 1
                    if verbose: print(f"line:{j}, column:{i} - {word_down}")
    return result


def check_down_forward(puzzle, word, verbose = False):
    result = 0
    w1, w2 = get_word_plus_reverse_as_list(word)

    for i in range(len(puzzle[0])):
        for j in range(len(puzzle)):
            if j + len(w1) <= len(puzzle) and i + len(w1) <= len(puzzle[0]):
                word_down_f = [ puzzle[j+idx][i+idx] for idx in range(len(w1)) ]

                if w1 == word_down_f or w2 == word_down_f: 
                    result = result + 1
                    if verbose: print(f"line:{j}, column:{i} - {word_down_f}")
    return result


def check_down_backward(puzzle, word, verbose = False):
    result = 0
    w1, w2 = get_word_plus_reverse_as_list(word)

    for i in range(len(puzzle[0])):
        for j in range(len(puzzle)):
            if j + len(w1) <= len(puzzle) and i - len(w1) >= -1:
                word_down_b = [ puzzle[j+idx][i-idx] for idx in range(len(w1)) ]

                if w1 == word_down_b or w2 == word_down_b: 
                    result = result + 1
                    if verbose: print(f"line:{j}, column:{i} - {word_down_b}")
    return result


COMBINATIONS = [
    ['M', 'M', 'S', 'S'],
    ['M', 'S', 'M', 'S'],
    ['S', 'M', 'S', 'M'],
    ['S', 'S', 'M', 'M'],
]


def check_x_mas(puzzle, verbose = False):
    result = 0

    for i in range(1, len(puzzle[0])-1):
        for j in range(1, len(puzzle)-1):
            if puzzle[j][i] == 'A':
                w = [puzzle[j-1][i-1], puzzle[j-1][i+1], puzzle[j+1][i-1], puzzle[j+1][i+1]]

                if w in COMBINATIONS: 
                    result = result + 1
                    if verbose: print(f"line:{j}, column:{i} - {w}")
    return result

                