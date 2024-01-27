#coding: utf-8
import random
from sudoku.sudoku_algorithms import *

def generate_sudoku():
    grid = np.zeros((9, 9), dtype=int)
    solve_sudoku(grid)
    return grid

def generate_sudoku_puzzle():
    grid = np.zeros((9, 9), dtype=int)
    solve_sudoku(grid)
    remove_numbers(grid, random.randint(20, 60))  # Retirer entre 20 et 60 chiffres
    return grid

def generate_difficult_sudoku(target_empty_cells=40):
    grid = np.zeros((9, 9), dtype=int)
    solve_sudoku(grid)
    remove_numbers_for_difficulty(grid, target_empty_cells=target_empty_cells)  # Ajustez ce nombre selon le niveau de difficulté souhaité
    return grid
