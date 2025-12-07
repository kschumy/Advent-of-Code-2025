from utils.advent_day import AdventDay
from utils.process_input import read_lines_to_matrix

DAY_NUMBER = 7
IS_EXAMPLE = False # set to False for real input, or True for example input

BEAM = "|"
SPLITTER = "^"
EMPTYS_SPACE = "."

day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
lines = read_lines_to_matrix(day.filename)
print(lines)

# Handle beam under "S"
total = 0
s_index = lines[0].index("S")
lines[1][s_index] = BEAM
# total += 1

for row in range(2, len(lines) - 1):
    for col in range(1, len(lines[0])):
        if lines[row][col] == SPLITTER:
            if lines[row - 1][col] == BEAM:
                total += 1
            lines[row + 1][col - 1] = BEAM
            lines[row + 1][col + 1] = BEAM
            lines[row][col - 1] = BEAM
            lines[row][col + 1] = BEAM
        elif lines[row - 1][col] == BEAM:
            lines[row][col] = BEAM

for r in lines:
    print("".join(r))
print(total)
 