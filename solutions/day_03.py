from collections import deque
from utils.process_input import read_lines

# INPUT_FILENAME = "day_03_example.txt"
# PART_ONE_EXPECTED_ANSWER = 357
# PART_TWO_EXPECTED_ANSWER = 3121910778619

INPUT_FILENAME = "day_03.txt"
# PART_ONE_EXPECTED_ANSWER = 17324
PART_TWO_EXPECTED_ANSWER = 171846613143331



    # In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
    # In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
    # In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
    # In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.


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

if __name__ == "__main__":
    total = 0
    lines = read_lines(INPUT_FILENAME)
    for line in lines:
        total += largest_possible_joltage(line, DIGIT_SPAN)
    print(total)
    print(f"EXPECTED ANSWER: {PART_TWO_EXPECTED_ANSWER}")
    print(f"ACTUAL ANSWER: {total}")
    print(f"ARE THEY EQUAL? {total == PART_TWO_EXPECTED_ANSWER}")

# DIGIT_SPAN = 12
# lines = read_lines(INPUT_FILENAME)
# # # print(lines)
# total = 0
# expected = [888911112111, 434234234278, 811111111119, 987654321111]
# for line in lines:
#     stack = list(line[:DIGIT_SPAN]) 
#     n = len(line)
#     for i in range(DIGIT_SPAN, n):
#         num_str = line[i]

#         pop_limit = len(line) - i
#         len(stack) + (n - i) > DIGIT_SPAN:





    # stack = list(line[:DIGIT_SPAN])   # or [] and feed first DIGIT_SPAN chars via the same loop
    # n = len(line)
    # for i in range(DIGIT_SPAN, n):
    #     ch = line[i]
    #     # can we pop the top to make room for a bigger ch?
    #     while stack and ch > stack[-1] and len(stack) + (n - i) > DIGIT_SPAN:
    #         stack.pop()
    #     if len(stack) < DIGIT_SPAN:
    #         stack.append(ch)
# result is ''.join(stack)
    # stack = line[:DIGIT_SPAN]
    # for i in range(DIGIT_SPAN, len(line)):
    #     temp_stack = [stack.pop(0)]
    #     while stack:
    #         if stack[0] > temp_stack[-1]:
    #             temp_stack.pop()
    #             while temp_stack:
    #                 stack.insert(0, temp_stack.pop())
    #             break
    #         else:
    #             temp_stack.append(stack.pop(0))
    #     if not stack:
    #         while temp_stack:
    #             dq.appendleft(temp_stack.pop())
    #     if line[i] > dq[-1]:
    #         dq.pop()
    #         dq.append(line[i])

    # stack = [line[0]]
    # for i in range(1, len(line)):
    #     pop_limit = len(line) - i
    #     while stack and line[i] > stack[-1] and pop_limit > 0:
    #         stack.pop()
    #         pop_limit -= 1
    #     stack.append(line[i])
#     print("ACTUAL:","".join(stack))
#     excepected = expected.pop()
#     print("EXPECTED:", excepected)
#     print(f"ARE THEY EQUAL? {int(''.join(stack)) == excepected}")
#     print("-----")
#     total += int("".join(stack))
# print(f"EXPECTED ANSWER: {PART_TWO_EXPECTED_ANSWER}")
# print(f"ACTUAL ANSWER: {total}")
# print(f"ARE THEY EQUAL? {total == PART_TWO_EXPECTED_ANSWER}")



# DIGIT_SPAN = 12
# lines = read_lines(INPUT_FILENAME)
# # # print(lines)
# total = 0
# expected = [888911112111, 434234234278, 811111111119, 987654321111]
# for line in lines:
#     curr = list(line[len(line) - DIGIT_SPAN:])
#     # print(curr)
#     for i in range(len(line) - DIGIT_SPAN - 1, -1, -1):
#         num_str = line[i]
#         for j in range(DIGIT_SPAN):
#             if num_str > curr[j]:
#                 # for k in range(j, DIGIT_SPAN):
#                 curr[0:j] = line[i:i + DIGIT_SPAN]
#                 curr = curr[0:DIGIT_SPAN]
#                 break
#     print("ACTUAL:","".join(curr))
#     excepected = expected.pop()
#     print("EXPECTED:", excepected)
#     print(f"ARE THEY EQUAL? {int(''.join(curr)) == excepected}")
#     print("-----")
#     total += int("".join(curr))
# print(f"EXPECTED ANSWER: {PART_TWO_EXPECTED_ANSWER}")
# print(f"ACTUAL ANSWER: {total}")
# print(f"ARE THEY EQUAL? {total == PART_TWO_EXPECTED_ANSWER}")
