import tkinter as tk
from sudoku import Sudoku

sudoku_number = input("Sudoku Numbers (from top-left to bottom-right order):")
new_sudoku = Sudoku(sudoku_number)
print("Sudoku original")
print(new_sudoku)
new_sudoku.solve()
print("Sudoku solved")
print(new_sudoku)
