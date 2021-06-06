from math import ceil
from collections import Counter

all_possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_camp = [
    [8, 0, 0, 1, 0, 3, 0, 4, 0],
    [0, 3, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 4, 0, 7, 3, 0, 0],
    [3, 0, 6, 0, 1, 2, 8, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 5, 8, 4, 0, 6, 0, 3],
    [0, 0, 8, 6, 0, 1, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 6, 0, 2, 0, 5, 0, 0, 8]
]


def text_to_camp(text):
    local_sudoku = [[0]*9]*9
    n = [st for st in str(text)]
    start, end = 0, 9
    for row in range(9):
        local_sudoku[row] = [int(x) for x in n[start:end]]
        start += 9
        end += 9
    return local_sudoku


def get_possibilities(x, y):
    counter_numbers = Counter(all_possible_numbers)
    row_possibilities = counter_numbers - Counter(sudoku_camp[x])
    column_possibilities = counter_numbers - Counter([row[y] for row in sudoku_camp])
    maximum_x, maximum_y = ceil((x+1)/3) * 3, ceil((y+1)/3) * 3
    counter_square = Counter([])

    # line too long for comprehension
    for column in range(maximum_y-3, maximum_y):
        for row in range(maximum_x-3, maximum_x):
            counter_square.update([sudoku_camp[row][column]])

    square_possibilities = counter_numbers - counter_square
    total_possibilities = row_possibilities & column_possibilities & square_possibilities
    return total_possibilities


def set_number(x, y):
    if sudoku_camp[x][y]:
        next_number = get_next_zero()
        if next_number:
            return set_number(next_number[0], next_number[1])
        else:
            return True
    else:
        possibilities = list(get_possibilities(x, y))
        if len(possibilities) >= 1:
            for poss in possibilities:
                sudoku_camp[x][y] = poss
                is_possible = False
                next_number = get_next_zero()
                if next_number:
                    is_possible = set_number(next_number[0], next_number[1])
                else:
                    return True
                if is_possible:
                    return True
            sudoku_camp[x][y] = 0
            return False

        else:
            return False


def get_next_zero():
    for row in range(9):
        for column in range(9):
            if not sudoku_camp[row][column]:
                return row, column
    return False


def show_camp(camp):
    for row in camp:
        print(row)


set_number(0, 0)
show_camp(sudoku_camp)
show_camp(text_to_camp("800103040030000007000407300306012804000000000705840603008601000200000030060205008"))
