from utils.advent_day import AdventDay
from utils.process_input import read_lines

DAY_NUMBER = 3
IS_EXAMPLE = False # set to False for real input, or True for example input

PART_ONE_DIGIT_SPAN = 2
PART_TWO_DIGIT_SPAN = 12

def largest_possible_joltage(s: str, digit_span: int) -> int:
    n = len(s)
    stack = []
    for i, ch in enumerate(s):
        while stack and ch > stack[-1] and len(stack) + (n - i) > digit_span:
            stack.pop()
        if len(stack) < digit_span:
            stack.append(ch)
    return int(''.join(stack[:digit_span]))

def get_total_voltage(lines, digit_span):
    total = 0
    for line in lines:
        total += largest_possible_joltage(line, digit_span)
    return total

if __name__ == "__main__":
    advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
    lines = read_lines(advent_day.get_filename())
    advent_day.print_both_results(
        get_total_voltage(lines, PART_ONE_DIGIT_SPAN),
        get_total_voltage(lines, PART_TWO_DIGIT_SPAN),
    )