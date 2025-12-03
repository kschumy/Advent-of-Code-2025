from utils.process_input import split_lines
## Example input from question prompt
# INPUT_FILENAME = "day_02_example.txt"
# PART_ONE_EXPECTED_ANSWER = 1227775554
# PART_TWO_EXPECTED_ANSWER = 4174379265
# PART_TWO_EXPECTED_ANSWER = 243

# 
INPUT_FILENAME = "day_02.txt"
PART_ONE_EXPECTED_ANSWER = 38158151648
PART_TWO_EXPECTED_ANSWER = 45283684555



### PART ONE SOLUTION ### 
# input = split_lines(INPUT_FILENAME).pop()
# # print(input)
# # print(len(input))
# arr = []
# for n in input:
#     ranges = n.split("-")
#     if len(ranges[0]) == len(ranges[1]) and len(ranges[0]) % 2 == 1:
#         continue
#     arr.append(ranges)
#     # print(f"{ranges[0]}\t{int(ranges[1]) - int(ranges[0])}")
# # print(arr)
# # print(len(arr))
#
#
# total = 0
# for r in arr:
#     start_str, end_str = r
#     start, end = int(start_str), int(end_str)
#     start_str = str(start)
#     if len(start_str) % 2 == 1:
#         # print(f"{start}")
#         start = 10 ** (len(start_str))
#         if start > end:
#             # print(f"{start} > {end}")
#             continue
#         start_str = str(start)
#     curr = start
#     print(f"Checking range {start}-{end}\t{end - start + 1} numbers")
#     for _ in range(end - start + 1):
#         print(f"  Checking {curr}")
#         curr_str = str(curr)
#         if len(curr_str) %2 == 1:
#             break
#         if curr_str[0:len(curr_str)//2] == curr_str[len(curr_str)//2:]:
#             print(curr)
#             total += curr
#         curr += 1
# print(f"Total: {total}\nExpected: {PART_ONE_EXPECTED_ANSWER}\nIs Correct: {total == PART_ONE_EXPECTED_ANSWER}")
### DO NOT DELETE ABOVE THIS LINE ###


is_part_one = True

input = split_lines(INPUT_FILENAME).pop()
arr = []
for n in input:
    ranges = n.split("-")
    if is_part_one and len(ranges[0]) == len(ranges[1]) and len(ranges[0]) % 2 == 1:
        continue
    arr.append(ranges)

total = 0
for r in arr:
    start_str, end_str = r
    start, end = int(start_str), int(end_str)
    start_str = str(start)
    curr = start
    for _ in range(end - start + 1):
        curr_str = str(curr)
        if is_part_one and len(curr_str) % 2 == 1:
            curr += 1
            continue
        section_len = 1
        if is_part_one:
            section_len = len(curr_str) // 2
        while section_len <= len(curr_str) // 2:
            if section_len == 0:
                curr += 1
                section_len += 1
                continue
            if not is_part_one and len(curr_str) % section_len != 0:
                section_len += 1
                continue
            found_one_invalid = False
            no_unmatching = True
            for i in range(section_len, len(curr_str), section_len):
                curr_sec = curr_str[i:i + section_len]
                prev_sec = curr_str[i - section_len:i]
                if curr_sec != prev_sec:
                    no_unmatching = False
                    break
            if no_unmatching:
                total += curr
                break
            section_len += 1
        curr += 1

if is_part_one:
    print(f"Total: {total}\nExpected: {PART_ONE_EXPECTED_ANSWER}\nIs Correct: {total == PART_ONE_EXPECTED_ANSWER}\nDiff: {PART_ONE_EXPECTED_ANSWER - total}")
else:
    print(f"Total: {total}\nExpected: {PART_TWO_EXPECTED_ANSWER}\nIs Correct: {total == PART_TWO_EXPECTED_ANSWER}\nDiff: {PART_TWO_EXPECTED_ANSWER - total}")


