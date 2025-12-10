from pathlib import Path

from shapely import Polygon, box
from utils.advent_day import AdventDay
from utils.process_input import split_lines_to_ints


DAY_NUMBER = 9
IS_EXAMPLE = False # set to False for real input, or True for example input

advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)

lines = split_lines_to_ints(advent_day.filename)



filled_shape = Polygon(lines)
# if IS_EXAMPLE:
#     print(filled_shape)
max_area = 0

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        x_1, y_1 = lines[i]
        x_2, y_2 = lines[j]

        min_x, max_x = min(x_1, x_2), max(x_1, x_2)
        min_y, max_y = min(y_1, y_2), max(y_1, y_2)
        rectangle = box(min_x, min_y, max_x, max_y)
        # if IS_EXAMPLE:
        #     print(rectangle)
        if filled_shape.contains(rectangle):
            area = (abs(x_1 - x_2) + 1) * (abs(y_1 - y_2) + 1) # TODO: change parentheses for part 1 b/c of bug here w/o them
            max_area = max(max_area, area)

print(max_area)
print(1560475800)




# matrix = []
# for _ in range(9):
#     matrix.append(["."] * 14)

# for x, y in lines:
#     print(f"Marking point at ({x}, {y})")
#     for row in matrix:
#         print("".join(row))
#     matrix[y][x] = "#"  
    
#     if x == 9 and y == 7:
#         print("==")
#         for row in matrix:
#             print("".join(row))
#     print("--------")

# for row in matrix:
#     print("".join(row))
    

# max_area = 0
# for i in range(0, len(lines) - 1):
#     print(lines[i])
#     pt_a_x, pt_a_y = lines[i]
#     for j in range(i + 1, len(lines)):
#         pt_b_x, pt_b_y = lines[j]
#         area = abs(pt_a_x - pt_b_x + 1) * abs(pt_a_y - pt_b_y + 1)
#         max_area = max(max_area, area)
# print(max_area)
        

