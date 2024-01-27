#coding: utf-8

from sudoku.sudoku_evaluate import *
import random
import numpy as np

def is_valid(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True
    
def solve_sudoku(grid, find_all_solutions=False):
    solution_count = 0

    def backtrack(row, col):
        nonlocal solution_count

        if row == 9:
            solution_count += 1
            return solution_count < 2 if find_all_solutions else True

        next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)
        if grid[row][col] != 0:
            return backtrack(next_row, next_col)

        for num in range(1, 10):
            if is_valid(grid, row, col, num):
                grid[row][col] = num
                if backtrack(next_row, next_col):
                    if not find_all_solutions:
                        return True
                grid[row][col] = 0

        return False

    backtrack(0, 0)
    return solution_count == 1 if find_all_solutions else solution_count > 0

def remove_numbers(grid, count):
    while count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != 0:
            grid[row][col] = 0
            count -= 1

def remove_numbers_for_difficulty(grid, target_empty_cells):
    while count_empty_cells(grid) < target_empty_cells:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if grid[row][col] != 0:
            backup = grid[row][col]
            grid[row][col] = 0

            # Vérifiez si la grille a une solution unique
            grid_copy = np.copy(grid)
            if not solve_sudoku(grid_copy, find_all_solutions=True):
                grid[row][col] = backup  # Restaurer le chiffre si plus d'une solution est trouvée

