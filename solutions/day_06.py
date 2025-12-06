from utils.advent_day import AdventDay
from utils.process_input import day_06_read_input


DAY_NUMBER = 6
IS_EXAMPLE = False # set to False for real input, or True for example input

# def add()

advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
nums_arr, op_arr = day_06_read_input(advent_day.filename)

print(nums_arr)
print(op_arr)

total = 0
for i in range(len(op_arr)):
    op = op_arr[i]
    curr_total = 0
    if op == "*":
        curr_total += 1
    
    for j in range(len(nums_arr)):
        print(nums_arr[j])
        if op == "*":
            curr_total *= nums_arr[j][i]
        else:
            curr_total += nums_arr[j][i]
    total += curr_total
print(total)