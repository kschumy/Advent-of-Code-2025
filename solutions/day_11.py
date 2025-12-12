from functools import lru_cache
from utils.advent_day import AdventDay
from utils.part import Part
from utils.process_input import read_devices_input


DAY_NUMBER = 11
IS_EXAMPLE = False

PART = Part.TWO

START_STR = "svr"
END_STR = "out"

FIRST_DEVICE = "fft"
SECOND_DEVICE = "dac"

advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)

lines = read_devices_input(advent_day.filename)

# print(lines)

# devices = {}
# for line in lines:
#     devices[line[0]] = line[1:]

devices = {}
for line in lines:
    devices[line[0]] = line[1:]

@lru_cache(maxsize=None)
def count_paths_part2(device: str, has_first_device, has_second_device):
    # print(f"\t{device}: {has_first_device} and {has_second_device}")
    if device == END_STR:
        # print(f"{has_first_device} and {has_second_device}")
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
        total += count_paths_part2(child_device, has_first_device, has_second_device)
    return total

total_paths = count_paths_part2(START_STR, False, False)
print(total_paths)

# ### PART 1 ###

# def count_paths(device: str):
#     if device == END_STR:
#         return 1
#     total = 0
#     for child_device in devices[device]:
#         total += count_paths(child_device)
#     return total

# total_paths = count_paths(START_STR)
# print(total_paths)
# ### END PART 1 ###