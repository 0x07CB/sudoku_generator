#coding: utf-8

import markdown
from sodoku_generate import *
from sodoku_evaluate import *


def sudoku_to_markdown(sudoku):
    markdown = "| " + " | ".join([""] * 10) + " |\n"  # En-tête du tableau
    markdown += "|-" + "|-".join(["--"] * 9) + "| |\n"  # Ligne de séparation
    
    for i, row in enumerate(sudoku):
        line = "| " + " | ".join(str(num) if num != 0 else " " for num in row) + " |"
        markdown += line + "\n"
        if i == 2 or i == 5:
            markdown += "|-" + "|-".join(["--"] * 9) + "| |\n"  # Ligne de séparation après chaque bloc de 3 lignes

    return markdown


sudoku = generate_difficult_sudoku(35)
difficulty = evaluate_difficulty(sudoku)
markdown_grid = sudoku_to_markdown(sudoku)
html_grid = markdown.markdown(markdown_grid)
print("Difficulté estimée:", difficulty)

