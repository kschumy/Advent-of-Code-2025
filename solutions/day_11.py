from utils.advent_day import AdventDay
from utils.process_input import read_devices_input


DAY_NUMBER = 11
IS_EXAMPLE = False

START_STR = "you"
END_STR = "out"

advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)

lines = read_devices_input(advent_day.filename)

print(lines)

devices = {}
for line in lines:
    devices[line[0]] = line[1:]

def count_paths(device: str):
    if device == END_STR:
        return 1
    total = 0
    for child_device in devices[device]:
        total += count_paths(child_device)
    return total

total_paths = count_paths(START_STR)
print(total_paths)