from collections import defaultdict
from utils.advent_day import AdventDay
from utils.process_input import read_lines_to_matrix

DAY_NUMBER = 7
IS_EXAMPLE = True # set to False for real input, or True for example input

BEAM = "|"
SPLITTER = "^"
EMPTYS_SPACE = "."


day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
lines = read_lines_to_matrix(day.filename)



beams = defaultdict(int)
s_index = lines[0].index("S") # starting position
beams[s_index] = 1

split_count = 0 # part 1

for row_index in range(1, len(lines)):
    row = lines[row_index]
    new_beams = defaultdict(int)
    for col_idx, timeline_count in beams.items():
        if col_idx < 0 or col_idx >= len(row):
            continue

        if row[col_idx] == SPLITTER:
            new_beams[col_idx - 1] += timeline_count
            new_beams[col_idx + 1] += timeline_count
            split_count += 1  # count the split for part 1
        elif row[col_idx] == BEAM or row[col_idx] == EMPTYS_SPACE:
            new_beams[col_idx] += timeline_count
    beams = new_beams
print(beams)
total_timeline_count = sum(beams.values()) # part 2

print(f"Part 1: {split_count}")
print(f"Part 2: {total_timeline_count}")

# Handle beam under "S"
# total = 0
# s_index = lines[0].index("S")
# lines[1][s_index] = BEAM

# COL_MAX = len(lines[0]) - 1
# ROW_MAX = len(lines) - 1
# # MAX = 20_000 # stop infinate recursion


# results = {}

# def count_timelines(row: int, col: int) -> int:
#     if row > ROW_MAX or col > COL_MAX or col < 0 or lines[row][col] == EMPTYS_SPACE:
#         return 0

#     coordinates = (row, col)
#     if coordinates in results:
#         # print(f"Using coordinates for {coordinates} - value: {results[coordinates]}")
#         return results[coordinates]

#     if lines[row][col] == BEAM:
#         result = count_timelines(row + 1, col)

#     elif lines[row][col] == SPLITTER:
#         left = count_timelines(row + 1, col - 1)
#         right = count_timelines(row + 1, col + 1)
#         result = left + right + 1

#     results[coordinates] = result
#     return result
# part_2_total = 1 # start with 1 for the beam under "S"
# part_2_total += count_timelines(1, s_index)
# # print(part_2_total)c
# expected = 1393669447690
# print(part_2_total == expected)
# print(f"Expected: {expected}")
# print(f"Actual: {part_2_total}")
# print(f"Difference: {expected - part_2_total}")
