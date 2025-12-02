from utils.process_input import read_lines
INPUT_FILENAME = "day_01.txt"
PART_ONE_EXPECTED_ANSWER = 1048
PART_TWO_EXPECTED_ANSWER = 6498

LEFT = "L"
MAX_NUM = 99
MIN_NUM = 0
ROTATION_AMOUNT = MAX_NUM + 1  # 0-99 inclusive
START_NUM = 50

def process_moves(lines) -> tuple[int, int]:
    curr_num = START_NUM
    passed_zero_count = 0
    is_zero_count = 0
    
    for line in lines:
        is_left = line[0] == LEFT
        amount = int(line[1:])
        
        passed_zero_count += amount // ROTATION_AMOUNT
        remainder = amount % ROTATION_AMOUNT
        
        if remainder:
            if is_left: # direction is "L"
                if curr_num != 0 and (curr_num - remainder) <= 0:
                    passed_zero_count += 1
                curr_num = (curr_num - remainder) % ROTATION_AMOUNT
            else: # direction is "R"
                if (curr_num + remainder) > MAX_NUM:
                    passed_zero_count += 1
                curr_num = (curr_num + remainder) % ROTATION_AMOUNT
        if curr_num == 0:
            is_zero_count += 1

    return (is_zero_count, passed_zero_count)

if __name__ == "__main__":
    lines = read_lines(INPUT_FILENAME)
    part1, part2 = process_moves(lines)

    results = [
        ("ONE", PART_ONE_EXPECTED_ANSWER, part1),
        ("TWO", PART_TWO_EXPECTED_ANSWER, part2),
    ]
    for name, expected, actual in results:
        print(
            f"PART {name} ANSWER:\n"
            f"\tExpected: {expected}\n"
            f"\tActual:   {actual}\n"
            f"\tIs Correct: {expected == actual}\n"
        )