from utils.advent_day import AdventDay
from utils.process_input import split_lines_to_ints


DAY_NUMBER = 9
IS_EXAMPLE = False # set to False for real input, or True for example input

advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)

lines = split_lines_to_ints(advent_day.filename)


print(lines)

max_area = 0
for i in range(0, len(lines) - 1):
    print(lines[i])
    pt_a_x, pt_a_y = lines[i]
    for j in range(i + 1, len(lines)):
        pt_b_x, pt_b_y = lines[j]
        area = abs(pt_a_x - pt_b_x + 1) * abs(pt_a_y - pt_b_y + 1)
        max_area = max(max_area, area)
print(max_area)
        

