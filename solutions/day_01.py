from utils.advent_day import AdventDay
from utils.process_input import read_lines

DAY_NUMBER = 1
IS_EXAMPLE = False # set to False for real input, or True for example input

LEFT = "L"
MAX_NUM = 99
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
    advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
    lines = read_lines(advent_day.get_filename())
    part1, part2 = process_moves(lines)
    advent_day.print_both_results(part1, part2)