from math import ceil
from collections import Counter

"""Sudoku example:
list:   [[8, 0, 0, 1, 0, 3, 0, 4, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 4, 0, 7, 3, 0, 0],
        [3, 0, 6, 0, 1, 2, 8, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 5, 8, 4, 0, 6, 0, 3],
        [0, 0, 8, 6, 0, 1, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 6, 0, 2, 0, 5, 0, 0, 8]]
        
text: 070060000000000006041708090003070400100205008002030600030602800900000507000080000
"""


class Sudoku:
    camp = [[0] * 9] * 9
    solved = False

    def __init__(self, sudoku_numbers: str):
        if len(sudoku_numbers) < 81:
            self.sudoku_numbers = "0" + sudoku_numbers
        else:
            self.sudoku_numbers = sudoku_numbers
        n = [st for st in str(sudoku_numbers)]
        start, end = 0, 9
        for row in range(9):
            self.camp[row] = [int(x) for x in n[start:end]]
            start += 9
            end += 9

    def __str__(self):
        text = ""
        for row in self.camp:
            for number in row:
                text += str(number) + "  "
            text += '\n'
        return text

    def get_possibilities(self, x, y):
        counter_numbers = Counter([1, 2, 3, 4, 5, 6, 7, 8, 9])
        row_possibilities = counter_numbers - Counter(self.camp[x])
        column_possibilities = counter_numbers - Counter([row[y] for row in self.camp])
        maximum_x, maximum_y = ceil((x + 1) / 3) * 3, ceil((y + 1) / 3) * 3
        counter_square = Counter([])

        for column in range(maximum_y - 3, maximum_y):
            for row in range(maximum_x - 3, maximum_x):
                counter_square.update([self.camp[row][column]])

        square_possibilities = counter_numbers - counter_square
        total_possibilities = row_possibilities & column_possibilities & square_possibilities
        return total_possibilities

    def set_numbers(self, x, y):
        if self.camp[x][y]:
            next_number = self.get_next_zero()
            if next_number:
                return self.set_numbers(next_number[0], next_number[1])
            else:
                return True
        else:
            possibilities = list(self.get_possibilities(x, y))
            if len(possibilities) >= 1:
                for poss in possibilities:
                    self.camp[x][y] = poss
                    next_number = self.get_next_zero()
                    if next_number:
                        is_possible = self.set_numbers(next_number[0], next_number[1])
                    else:
                        return True
                    if is_possible:
                        return True
                self.camp[x][y] = 0
                return False

            else:
                return False

    def get_next_zero(self):
        for row in range(9):
            for column in range(9):
                if not self.camp[row][column]:
                    return row, column
        return False

    def solve(self):
        if self.set_numbers(0, 0):
            self.solved = True
        else:
            print("Impossible to solve")


if __name__ == "__main__":
    sudoku = Sudoku("0"*81)
    sudoku.solve()
    print(sudoku)
