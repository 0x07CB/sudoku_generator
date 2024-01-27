#coding: utf-8

from sodoku import *

# import and write code to parse command line arguments
# import and write code to parse config file
import argparse
argparser = argparse.ArgumentParser(description="Sodoku solver")
argparser.add_argument("-d", "--difficulty", help="Difficulty of the sodoku puzzle to generate", type=int, default=40)
#argparser.add_argument("-s", "--size", help="Size of the sodoku puzzle to generate", type=int, default=9)
argparser.add_argument("-F", "--format", help="Format of the output file", type=str, default=".md")
argparser.add_argument("-f", "--filename", help="Name of the output file", type=str, default="sodoku")
argparser.add_argument("-p", "--path", help="Path of the output file", type=str, default="./")



# a class SodokuGenerator that generates a sodoku puzzle
class SodokuGenerator:
    def __init__(self):
        self.grid_sodoku = None
        self.sodoku_difficulty = None
        #self.sodoku_size = (9,9)
        #self.sodoku_box_size = (3,3)
        
    def set_difficulty(self, difficulty):
        self.sodoku_difficulty = difficulty
        return self

    def get_difficulty(self):
        return self.sodoku_difficulty

    def generate_grid(self):
        self.grid_sodoku = generate_difficult_sodoku(self.sodoku_difficulty)
        return self

    def evaluate_grid(self):
        return evaluate_difficult(self.grid_sodoku)

    def get_grid(self):
        return self.grid_sodoku

    def get_markdown_grid(self):
        return sodoku_to_markdown(self.grid_sodoku)

    def get_html_markdown_grid(self):
        return markdown.markdown(sodoku_to_markdown(self.grid_sodoku))

def sodoku_to_text(sodoku_grid):
    text_grid = ""
    for row in sodoku_grid:
        for col in row:
            text_grid += str(col)
        text_grid += "\n"
    return text_grid

def write_sodoku_to_file(sodoku_grid, filename, folderpath, file_format):
    if ( ( ".md" == file_format ) or ( ".html" == file_format ) ):
        with open(folderpath + filename + file_format, "w") as f:
            f.write(sodoku_grid)

    elif ( ".txt" == file_format ):
        with open(folderpath + filename + ".txt", "w") as f:
            f.write(sodoku_to_text(sodoku_grid))
    else:
        return None


def main():
    # parse command line arguments
    args = argparser.parse_args()
    # parse config file
    # generate a sodoku puzzle
    sodoku_generator = SodokuGenerator()
    sodoku_generator.set_difficulty(args.difficulty)
    sodoku_generator.generate_grid()

    # evaluate the puzzle
    evaluation_difficult = sodoku_generator.evaluate_grid()

    # write the puzzle to a file
    if ( ".md" == args.format ):
        write_sodoku_to_file(sodoku_generator.get_markdown_grid(), args.filename, args.path, args.format)
    elif ( ".html" == args.format ):
        write_sodoku_to_file(sodoku_generator.get_html_markdown_grid(), args.filename, args.path, args.format)
    elif ( ".txt" == args.format ):
        write_sodoku_to_file(sodoku_generator.get_grid(), args.filename, args.path, args.format)
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

