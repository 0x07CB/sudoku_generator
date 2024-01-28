# sudoku_generator
Sudoku generator python3 scripts



# Exemples:


## Générations de grilles de sudoku

Pour générer des grilles de Sudoku en Python, vous pouvez utiliser différentes approches. Voici deux exemples basiques: l'un utilisant un algorithme de backtracking (rétroaction) pour remplir la grille, et l'autre créant une grille complète puis retirant des chiffres aléatoirement pour créer le puzzle.

### Exemple 1: Algorithme de Backtracking

```python
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

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def generate_sudoku():
    grid = np.zeros((9, 9), dtype=int)
    solve_sudoku(grid)
    return grid

sudoku_grid = generate_sudoku()
print(sudoku_grid)
```

### Exemple 2: Créer une Grille Complète et Retirer des Chiffres

```python
import random

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

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def remove_numbers(grid, count):
    while count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != 0:
            grid[row][col] = 0
            count -= 1

def generate_sudoku_puzzle():
    grid = np.zeros((9, 9), dtype=int)
    solve_sudoku(grid)
    remove_numbers(grid, random.randint(20, 60))  # Retirer entre 20 et 60 chiffres
    return grid

sudoku_puzzle = generate_sudoku_puzzle()
print(sudoku_puzzle)
```

Ces deux exemples sont des points de départ. Vous pouvez ajuster la difficulté du Sudoku en changeant le nombre de chiffres retirés dans le deuxième exemple, ou en modifiant la stratégie de remplissage dans le premier exemple.


## Évaluation d’une grille de sudoku

Évaluer la difficulté d'une grille de Sudoku en Python est un peu plus complexe, car cela implique de tenir compte de plusieurs facteurs, tels que le nombre de cases vides, la distribution de ces vides, et les techniques nécessaires pour résoudre la grille. Il n'existe pas de méthode standard ou universellement acceptée pour cela, mais je peux vous donner un exemple basique qui utilise une approche simple pour estimer la difficulté.

L'exemple suivant évalue la difficulté en fonction du nombre de cases vides et de la distribution des nombres dans la grille :

### Exemple: Évaluation Basique de la Difficulté

```python
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

# Exemple d'utilisation
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

difficulty = evaluate_difficulty(sudoku)
print("Difficulté estimée:", difficulty)
```

Ce script est une approximation et ne prend pas en compte des aspects plus complexes du Sudoku comme les techniques de résolution avancées (par exemple, X-Wing, Swordfish, etc.). La difficulté réelle d'une grille pour un joueur humain peut varier considérablement en fonction de l'expérience et des compétences du joueur.


## Rendus de grilles de sudoku

Pour afficher une grille de Sudoku en Markdown et ensuite la convertir en HTML, vous pouvez suivre ces étapes :

1. **Créez une Représentation Markdown de la Grille de Sudoku :** Créez une chaîne de caractères représentant la grille en utilisant la syntaxe Markdown pour les tableaux.

2. **Convertissez le Markdown en HTML :** Utilisez un convertisseur Markdown vers HTML. En Python, vous pouvez utiliser des bibliothèques comme `markdown` ou `pandoc`.

Voici un exemple de code pour ces étapes :

### Étape 1 : Générer la Grille en Markdown

```python
def sudoku_to_markdown(sudoku):
    markdown = "| " + " | ".join([""] * 10) + " |\n"  # En-tête du tableau
    markdown += "|-" + "|-".join(["--"] * 9) + "| |\n"  # Ligne de séparation
    
    for i, row in enumerate(sudoku):
        line = "| " + " | ".join(str(num) if num != 0 else " " for num in row) + " |"
        markdown += line + "\n"
        if i == 2 or i == 5:
            markdown += "|-" + "|-".join(["--"] * 9) + "| |\n"  # Ligne de séparation après chaque bloc de 3 lignes

    return markdown

# Exemple d'utilisation
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    # Ajoutez les autres lignes de la grille ici...
]

markdown_grid = sudoku_to_markdown(sudoku)
print(markdown_grid)
```

### Étape 2 : Convertir le Markdown en HTML

Vous pouvez installer une bibliothèque comme `markdown` via pip (`pip install markdown`) et l'utiliser pour convertir le Markdown en HTML.

```python
import markdown

html_grid = markdown.markdown(markdown_grid)
print(html_grid)
```

Ce code vous donnera une représentation HTML de votre grille de Sudoku, que vous pouvez ensuite intégrer dans un document HTML ou afficher dans un navigateur.