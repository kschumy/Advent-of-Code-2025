
from utils.advent_day import AdventDay
from utils.process_input import read_lines_to_matrix_with_borders


DAY_NUMBER = 4
IS_EXAMPLE = False # set to False for real input, or True for example input

PAPER_CHAR = "@"
NON_PAPER_CHAR = "."
    
day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
# IMPORTANT: matrix has borders around it to simplify edge handling.
# There is one extra row at both the top and bottom, and one extra column on each side.
matrix = read_lines_to_matrix_with_borders(day.filename, NON_PAPER_CHAR)

paper_count = 0
while True:
    to_remove = []
    for row in range(1, len(matrix) - 1): # ignore border top and bottom
        for col in range(1, len(matrix[row]) - 1): # ignore border on row sides
            if matrix[row][col] != PAPER_CHAR:
                continue
            adjacent_paper_count = 0
            for row_offset in (-1, 0, 1):
                adjacent_paper_count += sum(matrix[row + row_offset][col + n] == PAPER_CHAR for n in (-1, 0, 1))
            adjacent_paper_count -= 1 # subtract self

            if adjacent_paper_count < 4:
                to_remove.append((row, col))
    if not to_remove:
        break
    paper_count += len(to_remove)
    for row, col in to_remove:
        matrix[row][col] = NON_PAPER_CHAR
print(paper_count)

