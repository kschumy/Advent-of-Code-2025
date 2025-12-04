
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

def is_paper(r, c, iteration):
    return int(matrix[r][c] == PAPER_CHAR or matrix[r][c] == iteration)

def count_top_or_bottom(r, c, iteration):
    curr_paper_count = 0
    for n in range(-1, 2):
        curr_paper_count += is_paper(r, c + n, iteration)
    return curr_paper_count

def count_left_and_right(r, c, iteration):
    return count_top_or_bottom(r, c, iteration) - 1 # subtract self
    # curr_paper_count = 
    # return is_paper(r, c + 1) + is_paper(r, c + ) int(matrix[r][c - 1] == PAPER_CHAR) + int(int(matrix[r][c + 1] == PAPER_CHAR))

paper_count = 0
curr_iteration = 1
has_changed = True
while has_changed:
    has_changed = False
    for row in range(1, len(matrix) - 1): # ignore border top and bottom
        for col in range(1, len(matrix[1]) - 1): # ignore border on row sides
            if matrix[row][col] != PAPER_CHAR:
                continue
            adjacent_paper_count = count_left_and_right(row, col, curr_iteration)
            adjacent_paper_count += count_top_or_bottom(row - 1, col, curr_iteration)
            adjacent_paper_count += count_top_or_bottom(row + 1, col, curr_iteration)
            if adjacent_paper_count < 4:
                paper_count += 1
                has_changed = True
                matrix[row][col] = curr_iteration
    curr_iteration += 1
print(paper_count)

