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


def get_possibilities(x, y):
    counter_numbers = Counter(all_possible_numbers)
    row_possibilities = counter_numbers - Counter(sudoku_camp[x])
    column_possibilities = counter_numbers - Counter([row[y] for row in sudoku_camp])
    maximum_x, maximum_y = ceil((x+1)/3) * 3, ceil((y+1)/3) * 3
    counter_square = Counter([])

    # line too long for comprehension
    for column in range(maximum_y-2, maximum_y):
        for row in range(maximum_x-2, maximum_x):
            counter_square.update([sudoku_camp[row][column]])

    square_possibilities = counter_numbers - counter_square
    total_possibilities = row_possibilities & column_possibilities & square_possibilities
    return total_possibilities


def set_number(x, y):
    if not sudoku_camp[x][y]:
        possible_numbers = list(get_possibilities(x, y))
        if len(possible_numbers) < 1:
            return False
        sudoku_camp[x][y] = possible_numbers[0]
        if x+1 < 9:
            return set_number(x+1, y)
        elif y+1 < 9:
            return set_number(x, y+1)
        else:
            return True


print(list(get_possibilities(0, 1)))