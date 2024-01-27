#coding: utf-8

import numpy as np

def count_empty_cells(sudoku):
    return sum(np.count_nonzero(row == 0) for row in sudoku)

def count_unique_numbers(sudoku):
    unique_numbers = set()
    for row in sudoku:
        unique_numbers.update(row)
    return len(unique_numbers) - (1 if 0 in unique_numbers else 0)

def evaluate_difficulty(sudoku):
    empty_cells = count_empty_cells(sudoku)
    unique_numbers = count_unique_numbers(sudoku)

    if empty_cells > 60:
        return "Très facile"
    elif 50 < empty_cells <= 60:
        return "Facile"
    elif 36 < empty_cells <= 50:
        return "Moyen"
    elif 32 < empty_cells <= 36 and unique_numbers > 7:
        return "Difficile"
    else:
        return "Très difficile"

