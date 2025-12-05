from utils.advent_day import AdventDay
from utils.process_input import read_input_with_ranges_and_integers


DAY = 5
IS_EXAMPLE = False
day = AdventDay(DAY, IS_EXAMPLE)

ranges, values = read_input_with_ranges_and_integers(day.filename)
print(ranges)
sorted_ranges = sorted(ranges, key=lambda x: (x[1], x[0]))
print(sorted_ranges)
values.sort()
print(values)

fresh_count = 0
# range_index = len(sorted_ranges) - 1
for i in range(len(values) - 1, -1, -1):
    val = values[i]
    range_index = len(sorted_ranges) - 1
    while range_index >= 0 and not (ranges[range_index][0] <= val <= ranges[range_index][1]) :
        range_index -= 1
    if range_index >= 0 and ranges[range_index][0] <= val <= ranges[range_index][1]:
        print(f"fresh: {val}")
        fresh_count += 1
print(fresh_count)