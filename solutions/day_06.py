from collections import deque
from utils.advent_day import AdventDay
from utils.process_input import day_06_read_input, day_06_read_input_part_2
from math import prod

DAY_NUMBER = 6
IS_EXAMPLE = False # set to False for real input, or True for example input
# 6957525317641
# def add()

advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
nums_arr, op_arr = day_06_read_input(advent_day.filename)

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
print(full_lines)
full_lines.pop()
ans = 0
running_total = 0
if op_arr[op_index] == "*":
    running_total = 1
for col in range(len(full_lines[0])):
    curr_col = []
    for row in range(len(full_lines)):
        curr_col.append(full_lines[row][col])
    line_str = "".join(curr_col).strip()
    if len(line_str) == 0:
        ans += running_total
        op_index += 1
        if op_arr[op_index] == "*":
            running_total = 1
        else:
            running_total = 0
        continue
    if op_arr[op_index] == "*":
        running_total *= int(line_str)
    else:
        running_total += int(line_str)

ans += running_total
print(ans)
print(f"expected: 3263827")
print(3263827 == ans)

# ans = 0
# while nums_col_arrs:
#     # print(nums_arr.pop())


#     curr_arr = nums_col_arrs.pop()
#     print(curr_arr)
#     opp = op_arr.pop()
    
#     arr = []
#     for i in range(len(curr_arr)):
#         arr.append(str(curr_arr[i]))
#     #    dq.append(str(curr_arr))
#     # stack = []
#     j = 0
#     # print(arr)
#     # print("----")
#     curr_total = 0
#     if opp == "*":
#             curr_total = 1
#     found_one = True
#     while found_one:
#         found_one = False
#         curr = []
#         # curr_total = 0
#         for number in arr:
#             # print(f"number: {number}")
#             if len(number) > j:
#                 found_one = True
#                 curr.append(number[j])
#         if found_one:
#             str_num = "".join(curr)
#             if str_num == "":
#                 print("WHAT HAPPENED")
#             else:
#                 # print(str_num)
#                 print(int(str_num))
#                 if opp == "*":
#                     curr_total *= int(str_num)
#                 else:
#                     curr_total += int(str_num)
#                 # ans += int(str_num)
#                 # print(ans)
#                 print("----")
#                 j += 1
#     print(f"curr_total: {curr_total}")
#     ans += curr_total
# print(ans)
# print(f"expected: 3263827")
# print(3263827 == ans)
    # while dq or stack:
    #     if not dq:
    #         dq = stack
    #     if stack:
    #         stack = []


# ['6', '98', '215', '314']
# ----
# 6923
# 811
# 54
# ['45', '64', '387', '23']
# ----
# 4632
# 5483
# 7
# ['123', '328', '51', '64']
# ----
# 1356
# 2214
# 38
# 21518
# expected: 3263827

#     The rightmost problem is 4 + 431 + 623 = 1058
#     The second problem from the right is 175 * 581 * 32 = 3253600
#     The third problem from the right is 8 + 248 + 369 = 625
#     Finally, the leftmost problem is 356 * 24 * 1 = 8544






