
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
print(matrix)
# start_index = 1
def count_top_or_bottom(r, c):
    curr_paper_count = 0
    for n in range(-1, 2):
        curr_paper_count += int(matrix[r][c + n] == PAPER_CHAR)
    return curr_paper_count

def count_left_and_right(r, c):
    return int(matrix[r][c - 1] == PAPER_CHAR) + int(int(matrix[r][c + 1] == PAPER_CHAR))

paper_count = 0
for row in range(1, len(matrix) - 1): # ignore border top and bottom
    for col in range(1, len(matrix[1]) - 1): # ignore border on row sides
        if matrix[row][col] != PAPER_CHAR:
            continue
        adjacent_paper_count = count_left_and_right(row, col)
        adjacent_paper_count += count_top_or_bottom(row - 1, col)
        # if adjacent_paper_count > 4:
        #     continue
        adjacent_paper_count += count_top_or_bottom(row + 1, col)
        if adjacent_paper_count < 4:
            paper_count += 1
print(paper_count)

