from utils.advent_day import AdventDay
from utils.process_input import read_lines_with_last_line_removed, read_lines_with_numbers_and_strings
from math import prod

DAY_NUMBER = 6
IS_EXAMPLE = False # set to False for real input, or True for example input

MULTIPLY_OP = "*"

def is_multiply(op: str) -> bool:
    return op == MULTIPLY_OP

# Part 1
def vertical_calculation(nums, operations):
    nums_by_col = [list(col) for col in zip(*nums)]
    total = 0
    for i in range(len(operations)):
        total += prod(nums_by_col[i]) if is_multiply(operations[i]) else sum(nums_by_col[i])
    return total

# Part 2
def column_calculation(full_lines, operations):
    op_index = 0
    reset_running_total = lambda op: int(is_multiply(op))
    running_total = reset_running_total(operations[op_index])
    ans = 0
    for col in range(len(full_lines[0])):
        line_str = "".join([full_lines[row][col].strip() for row in range(len(full_lines))])
        if len(line_str) == 0: # blank line indicates end of numbers for that column group
            ans += running_total
            op_index += 1
            running_total = reset_running_total(operations[op_index])
        elif is_multiply(operations[op_index]):
            running_total *= int(line_str)
        else:
            running_total += int(line_str)
    ans += running_total
    return ans

if __name__ == "__main__":
    advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
    nums, operations = read_lines_with_numbers_and_strings(advent_day.filename)
    full_lines = read_lines_with_last_line_removed(advent_day.filename)
    advent_day.print_both_results(
        vertical_calculation(nums, operations),
        column_calculation(full_lines, operations),
    )