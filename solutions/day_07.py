from utils.advent_day import AdventDay
from utils.process_input import read_lines_to_matrix

DAY_NUMBER = 7
IS_EXAMPLE = False # set to False for real input, or True for example input

BEAM = "|"
SPLITTER = "^"
EMPTYS_SPACE = "."



day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
lines = read_lines_to_matrix(day.filename)
# print(lines)


# Handle beam under "S"
total = 0
s_index = lines[0].index("S")
lines[1][s_index] = BEAM


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

print(total)

# Handle beam under "S"
# total = 0
# s_index = lines[0].index("S")
# lines[1][s_index] = BEAM

COL_MAX = len(lines[0]) - 1
ROW_MAX = len(lines) - 1
# MAX = 20_000 # stop infinate recursion


results = {}

def count_timelines(row: int, col: int) -> int:
    if row > ROW_MAX or col > COL_MAX or col < 0 or lines[row][col] == EMPTYS_SPACE:
        return 0

    coordinates = (row, col)
    if coordinates in results:
        # print(f"Using coordinates for {coordinates} - value: {results[coordinates]}")
        return results[coordinates]

    if lines[row][col] == BEAM:
        result = count_timelines(row + 1, col)

    elif lines[row][col] == SPLITTER:
        left = count_timelines(row + 1, col - 1)
        right = count_timelines(row + 1, col + 1)
        result = left + right + 1

    results[coordinates] = result
    return result
part_2_total = 1 # start with 1 for the beam under "S"
part_2_total += count_timelines(1, s_index)
# print(part_2_total)
expected = 1393669447690
print(part_2_total == expected)
print(f"Expected: {expected}")
print(f"Actual: {part_2_total}")
print(f"Difference: {expected - part_2_total}")
