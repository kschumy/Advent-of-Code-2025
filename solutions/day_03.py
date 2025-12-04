from collections import deque
from utils.process_input import read_lines

# INPUT_FILENAME = "day_03_example.txt"
# PART_ONE_EXPECTED_ANSWER = 357
# PART_TWO_EXPECTED_ANSWER = 3121910778619

INPUT_FILENAME = "day_03.txt"
PART_ONE_EXPECTED_ANSWER = 17324
PART_TWO_EXPECTED_ANSWER = 171846613143331



## PART ONE SOLUTION ###
# lines = read_lines(INPUT_FILENAME)
# # print(lines)
# total = 0
# for line in lines:
#     curr_total = [line[0], line[1]]
#     # print(curr_total)
#     for i in range(1, len(line) - 1):
#         if line[i] > curr_total[0]:
#             curr_total = [line[i], line[i + 1]]
#         elif line[i] > curr_total[1]:
#             curr_total[1] = line[i]
#     curr_total[1] = max(curr_total[1], line[-1])
#     total += int("".join(curr_total))
# print(total)
# ## END PART ONE SOLUTION ###

DIGIT_SPAN = 12

def largest_possible_joltage(s: str, digit_span: int) -> int:
    n = len(s)
    stack = []
    for i, ch in enumerate(s):
        while stack and ch > stack[-1] and len(stack) + (n - i) > digit_span:
            stack.pop()
        if len(stack) < digit_span:
            stack.append(ch)
    return int(''.join(stack[:digit_span]))

def get_part_one_and_part_two_answers(lines):
    part_one_total = 0
    part_two_total = 0
    for line in lines:
        part_one_total += largest_possible_joltage(line, 2)
        part_two_total += largest_possible_joltage(line, DIGIT_SPAN)
    return part_one_total, part_two_total

if __name__ == "__main__":
    # total = 0
    # lines = read_lines(INPUT_FILENAME)
    # for line in lines:
    #     total += largest_possible_joltage(line, DIGIT_SPAN)
    # print(total)
    # print(f"EXPECTED ANSWER: {PART_TWO_EXPECTED_ANSWER}")
    # print(f"ACTUAL ANSWER: {total}")
    # print(f"ARE THEY EQUAL? {total == PART_TWO_EXPECTED_ANSWER}")

    part_one_result, part_two_result = get_part_one_and_part_two_answers(read_lines(INPUT_FILENAME))
    results = [
        ("ONE", PART_ONE_EXPECTED_ANSWER, part_one_result),
        ("TWO", PART_TWO_EXPECTED_ANSWER, part_two_result),
    ]
    for name, expected, actual in results:
        print(
            f"PART {name} ANSWER:\n"
            f"\tExpected: {expected}\n"
            f"\tActual:   {actual}\n"
            f"\tIs Correct: {expected == actual}\n"
        )
