from utils.advent_day import AdventDay
from utils.process_input import read_input_with_ranges_and_integers


DAY = 5
IS_EXAMPLE = False
day = AdventDay(DAY, IS_EXAMPLE)

ranges, values = read_input_with_ranges_and_integers(day.filename)
print(ranges)
sorted_ranges = sorted(ranges, key=lambda x: [x[1], x[0]])
print(sorted_ranges)
values.sort()
print(values)

combined_ranges = [sorted_ranges.pop()]
while sorted_ranges:
    curr = sorted_ranges.pop()
    prev_start, prev_end = combined_ranges[-1]
    if prev_start <= curr[1] <= prev_end:
        combined_ranges[-1][0] = min(prev_start, curr[0])
    else:
        combined_ranges.append(curr)

total = 0
for c in combined_ranges:
    total += c[1] - c[0] + 1
print(total)


### PART ONE ###
# fresh_count = 0
# # range_index = len(sorted_ranges) - 1
# for i in range(len(values) - 1, -1, -1):
#     val = values[i]
#     range_index = len(sorted_ranges) - 1
#     while range_index >= 0 and not (ranges[range_index][0] <= val <= ranges[range_index][1]) :
#         range_index -= 1
#     if range_index >= 0 and ranges[range_index][0] <= val <= ranges[range_index][1]:
#         print(f"fresh: {val}")
#         fresh_count += 1
# print(fresh_count)
### END PART ONE ###