# TODO: fix this after finishing AofC. Needs to work for change in examples for parts

from functools import lru_cache
from utils.advent_day import AdventDay
from utils.part import Part
from utils.process_input import read_devices_input


DAY_NUMBER = 11
IS_EXAMPLE = True

# Part 1
PART_ONE_START_STR = "you" 

# Part 2
PART_TWO_START_STR = "svr"
FIRST_DEVICE = "fft"
SECOND_DEVICE = "dac"

# Both parts
END_STR = "out"

# advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)

# lines = read_devices_input(advent_day.filename)

# print(lines)

# devices = {}
# for line in lines:
#     devices[line[0]] = line[1:]



@lru_cache(maxsize=None)
def count_paths_part2(devices, device: str, has_first_device, has_second_device):
    if device == END_STR:
        return int(has_first_device and has_second_device)
    elif device == SECOND_DEVICE:
        if not has_first_device:
            return 0
        has_second_device = True
    elif device == FIRST_DEVICE:
        if has_second_device:
            return 0
        has_first_device = True
    total = 0
    for child_device in devices[device]:
        total += count_paths_part2(devices, child_device, has_first_device, has_second_device)
    return total

# total_paths = count_paths_part2(START_STR, False, False)
# print(total_paths)

# Part 1
def count_paths(devices, device: str):
    if device == END_STR:
        return 1
    total = 0
    for child_device in devices[device]:
        total += count_paths(devices, child_device)
    return total

# total_paths = 
# print(total_paths)

# FIXME: currently broken from different input for example
if __name__ == "__main__":
    advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
    devices_input = read_devices_input(advent_day.filename) # Part 2 for both example and real input
    devices = {}
    for line in devices_input:
        devices[line[0]] = line[1:]
    print(devices)
    if IS_EXAMPLE:
        devices_input_part_1 = read_devices_input(advent_day.get_filename(Part.ONE))

    advent_day.print_both_results(
        count_paths(devices, PART_ONE_START_STR), # PART 1
        count_paths_part2(devices, PART_TWO_START_STR, False, False), # PART 2
    )