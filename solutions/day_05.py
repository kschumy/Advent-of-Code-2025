from utils.advent_day import AdventDay
from utils.process_input import read_input_with_ranges_and_integers

DAY_NUMBER = 5
IS_EXAMPLE = False # set to False for real input, or True for example input

# Part 1
# Assumes ranges are sorted and overlapping ranges have been merged 
def count_available_fresh_ids(ranges: list[list[int]], values: list[int]) -> int:
    values.sort()
    n = len(values)
    vi = 0
    total = 0
    for start_range, end_range in ranges:
        while vi < n and values[vi] < start_range:
            vi += 1
        while vi < n and values[vi] <= end_range:
            total += 1
            vi += 1
    return total

# Part 2
# Assumes overlapping ranges have been merged
def count_ids_from_merged_ranges(ranges):
    return sum(end_range - start_range + 1 for start_range, end_range in ranges)

# Sorts and merges overlapping ranges
def merge_ranges(ranges: list[list[int]]) -> list[list[int]]:
    ranges.sort()
    merged = []
    for start_range, end_range in ranges:
        if not merged or start_range > merged[-1][1] + 1:
            merged.append([start_range, end_range])
        else:
            merged[-1][1] = max(merged[-1][1], end_range)
    return merged

if __name__ == "__main__":
    advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
    ranges, values = read_input_with_ranges_and_integers(advent_day.filename)
    
    merged_ranges = merge_ranges(ranges)
    
    # part 1: fresh values count
    part1 = count_available_fresh_ids(merged_ranges, values)
    # part 2: total number of ids covered by merged ranges
    part2 = count_ids_from_merged_ranges(merged_ranges)
   
    advent_day.print_both_results(part1, part2)