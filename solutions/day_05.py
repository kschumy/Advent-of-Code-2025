from utils.advent_day import AdventDay
from utils.process_input import read_input_with_ranges_and_integers


DAY_NUMBER = 5
IS_EXAMPLE = False
day = AdventDay(DAY_NUMBER, IS_EXAMPLE)



# combined_ranges = [sorted_ranges.pop()]
# while sorted_ranges:
#     curr = sorted_ranges.pop()
#     prev_start, prev_end = combined_ranges[-1]
#     if prev_start <= curr[1] <= prev_end:
#         combined_ranges[-1][0] = min(prev_start, curr[0])
#     else:
#         combined_ranges.append(curr)

# total = 0
# for c in combined_ranges:
#     total += c[1] - c[0] + 1
# print(total)


## PART ONE ###
# def part_one_solution(ranges: list[list[int]], values: list[int]):# -> int:
#     ranges_total = 0
#     fresh_count = 0
#     # range_index = len(sorted_ranges) - 1
#     for i in range(len(ranges) - 1, -1, -1):
#         c = ranges[i]
#         ranges_total += c[1] - c[0] + 1
#         val = values[i]
#         range_index = len(ranges) - 1
#         while range_index >= 0 and not (ranges[range_index][0] <= val <= ranges[range_index][1]) :
#             range_index -= 1
#         if range_index >= 0 and ranges[range_index][0] <= val <= ranges[range_index][1]:
#             print(f"fresh: {val}")
#             fresh_count += 1
#     return ranges_total, fresh_count
## END PART ONE ###

def get_available_and_total_fresh(ranges: list[list[int]], values: list[int]):# -> int, int:
    values_total = 0
    ranges_total = 0
    for c in ranges:
        ranges_total += c[1] - c[0] + 1
        print(f"Range: {c[0]}-{c[1]}")
        while values and values[-1] > c[1]:
            print(f"No: {values.pop()}")
        while values and c[0] <= values[-1] <= c[1]:
            values_total += 1
            print(f"Yes: {values.pop()}")
    print(values)
    return (ranges_total, values_total)


def sort_and_combine_ranges(ranges: list[list[int]]) -> list[list[int]]:
    print(ranges)
    sorted_ranges = sorted(ranges, key=lambda x: [x[1], x[0]])
    combined_ranges = [sorted_ranges.pop()]
    while sorted_ranges:
        curr = sorted_ranges.pop()
        prev_start, prev_end = combined_ranges[-1]
        if prev_start <= curr[1] <= prev_end:
            combined_ranges[-1][0] = min(prev_start, curr[0])
        else:
            combined_ranges.append(curr)
    print(combined_ranges)
    return combined_ranges

if __name__ == "__main__":
    advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
    ranges, values = read_input_with_ranges_and_integers(day.filename)

    combined_ranges = sort_and_combine_ranges(ranges)
    values.sort(reverse=False)
    ranges_total, values_total = get_available_and_total_fresh(combined_ranges, values)
    print(ranges_total)
    advent_day.print_both_results(
        values_total, ranges_total
    )