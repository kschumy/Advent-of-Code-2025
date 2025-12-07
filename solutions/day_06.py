from collections import deque
from utils.advent_day import AdventDay
from utils.process_input import day_06_read_input, day_06_read_input_part_2
from math import prod

DAY_NUMBER = 6
IS_EXAMPLE = True # set to False for real input, or True for example input
MULTIPLY_OP = "*"
# 6957525317641
# def add()

advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
nums_arr, op_arr = day_06_read_input(advent_day.filename)

def get_running_total_start(op: str) -> int:
    if op == MULTIPLY_OP:
        return 1
    return 0


# print(nums_arr)
# print(op_arr)

# nums_col_arrs = []
# for i in range(len(nums_arr[0])):
#     curr_arr = []
#     for j in range(len(nums_arr)):
#        curr_arr.append(nums_arr[j][i])
#     nums_col_arrs.append(curr_arr)
# print(nums_col_arrs)

### PART 1 ###
# total = 0
# for i in range(len(op_arr)):
#     if op_arr[i] == "*":
#         total += prod(nums_col_arrs[i])
#     else:
#         total += sum(nums_col_arrs[i])
# print(total)
### END PART 1 ###

op_index = 0
full_lines = day_06_read_input_part_2(advent_day.filename)
ans = 0
running_total = get_running_total_start(op_arr[op_index])
for col in range(len(full_lines[0])):
    line_str = "".join([full_lines[row][col].strip() for row in range(len(full_lines))])
    if len(line_str) == 0: # blank line indicates end of numbers for that column group
        ans += running_total
        op_index += 1
        running_total = get_running_total_start(op_arr[op_index])
        continue
    if op_arr[op_index] == "*":
        running_total *= int(line_str)
    else:
        running_total += int(line_str)

ans += running_total
print(ans)
print(f"expected: 3263827")
print(3263827 == ans)
