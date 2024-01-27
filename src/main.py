#coding: utf-8

import markdown

def sudoku_to_markdown(sudoku):
    markdown = "| " + " | ".join([""] * 10) + " |\n"  # En-tête du tableau
    markdown += "|-" + "|-".join(["--"] * 9) + "| |\n"  # Ligne de séparation
    
    for i, row in enumerate(sudoku):
        line = "| " + " | ".join(str(num) if num != 0 else " " for num in row) + " |"
        markdown += line + "\n"
        if i == 2 or i == 5:
            markdown += "|-" + "|-".join(["--"] * 9) + "| |\n"  # Ligne de séparation après chaque bloc de 3 lignes

    return markdown

import sudoku.sudoku_generate as sudoku_generate
import sudoku.sudoku_evaluate as sudoku_evaluate

# import and write code to parse command line arguments
# import and write code to parse config file
import argparse
argparser = argparse.ArgumentParser(description="Sudoku solver")
argparser.add_argument("-d", "--difficulty", help="Difficulty of the sudoku puzzle to generate", type=int, default=40)
#argparser.add_argument("-s", "--size", help="Size of the sudoku puzzle to generate", type=int, default=9)
argparser.add_argument("-F", "--format", help="Format of the output file", type=str, default=".md")
argparser.add_argument("-f", "--filename", help="Name of the output file", type=str, default="sudoku")
argparser.add_argument("-p", "--path", help="Path of the output file", type=str, default="./")



# a class SudokuGenerator that generates a sudoku puzzle
class SudokuGenerator:
    def __init__(self):
        self.grid_sudoku = None
        self.sudoku_difficulty = None
        #self.sudoku_size = (9,9)
        #self.sudoku_box_size = (3,3)
        
    def set_difficulty(self, difficulty):
        self.sudoku_difficulty = difficulty
        return self

    def get_difficulty(self):
        return self.sudoku_difficulty

    def generate_grid(self):
        self.grid_sudoku = sudoku_generate.generate_difficult_sudoku(self.sudoku_difficulty)
        return self

    def evaluate_grid(self):
        return sudoku_evaluate.evaluate_difficulty(self.grid_sudoku)

    def get_grid(self):
        return self.grid_sudoku

    def get_markdown_grid(self):
        return sudoku_to_markdown(self.grid_sudoku)

    def get_html_markdown_grid(self):
        return markdown.markdown(sudoku_to_markdown(self.grid_sudoku))

def sudoku_to_text(sudoku_grid):
    text_grid = ""
    for row in sudoku_grid:
        for col in row:
            text_grid += str(col)
        text_grid += "\n"
    return text_grid

def write_sudoku_to_file(sudoku_grid, filename, folderpath, file_format):
    if ( ( ".md" == file_format ) or ( ".html" == file_format ) ):
        with open(folderpath + filename + file_format, "w") as f:
            f.write(sudoku_grid)

    elif ( ".txt" == file_format ):
        with open(folderpath + filename + ".txt", "w") as f:
            f.write(sudoku_to_text(sudoku_grid))
    else:
        return None


def main():
    # parse command line arguments
    args = argparser.parse_args()
    # parse config file
    # generate a sudoku puzzle
    sudoku_generator = SudokuGenerator()
    sudoku_generator.set_difficulty(args.difficulty)
    sudoku_generator.generate_grid()

    # evaluate the puzzle
    evaluation_difficult = sudoku_generator.evaluate_grid()

    # write the puzzle to a file
    if ( ".md" == args.format ):
        write_sudoku_to_file(sudoku_generator.get_markdown_grid(), args.filename, args.path, args.format)
    elif ( ".html" == args.format ):
        write_sudoku_to_file(sudoku_generator.get_html_markdown_grid(), args.filename, args.path, args.format)
    elif ( ".txt" == args.format ):
        write_sudoku_to_file(sudoku_generator.get_grid(), args.filename, args.path, args.format)
    else:
        print("Format not supported")
        exit(1)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		print("{e}".format(e=e))
		exit(1)
	exit(0)

