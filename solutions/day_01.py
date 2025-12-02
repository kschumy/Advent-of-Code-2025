from utils.process_input import read_lines

PART_ONE_EXPECTED_ANSWER = 1048
PART_TWO_EXPECTED_ANSWER = 6498
INPUT_FILENAME = "day_01.txt"

START_NUM = 50
MAX_NUM = 99
MIN_NUM = 0
ROTATION_AMOUNT = MAX_NUM + 1  # 0-99 inclusive
LEFT = "L"

curr_num = START_NUM

passed_zero_count = 0
is_zero_count = 0

for line in read_lines(INPUT_FILENAME):
    is_left = line[0] == LEFT
    amount = int(line[1:])
    
    passed_zero_count += amount // ROTATION_AMOUNT
    remainder = amount % ROTATION_AMOUNT
    
    if is_left:
        if curr_num > remainder:
            curr_num -= remainder
        else:
            if curr_num != 0:
                passed_zero_count += 1
            beyond_zero = remainder - curr_num
            curr_num = ROTATION_AMOUNT - beyond_zero
            if curr_num > MAX_NUM:
                curr_num = 0
    else: # direction is "R"
        if curr_num + remainder <= MAX_NUM:
            curr_num += remainder
        else:
            if curr_num != 0:
                passed_zero_count += 1
            beyond_zero = curr_num + remainder
            curr_num = beyond_zero - ROTATION_AMOUNT
    if curr_num == 0:
        is_zero_count += 1

for result in [("ONE", PART_ONE_EXPECTED_ANSWER, is_zero_count), ("TWO", PART_TWO_EXPECTED_ANSWER, passed_zero_count)]:
    print(f"PART {result[0]} ANSWER:\n\tExpected: {result[1]}\n\tActual: {result[2]}\n\tIs Correct: {result[1] == result[2]}\n")