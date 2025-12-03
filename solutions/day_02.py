from utils.process_input import split_lines
## Example input from question prompt
# INPUT_FILENAME = "day_02_example.txt"
# PART_ONE_EXPECTED_ANSWER = 1227775554
# PART_TWO_EXPECTED_ANSWER = 

# 
INPUT_FILENAME = "day_02.txt"
PART_ONE_EXPECTED_ANSWER = 0
# PART_TWO_EXPECTED_ANSWER = 648


# 11-22 has two invalid IDs, 11 and 22.
# 95-115 has one invalid ID, 99.
# 998-1012 has one invalid ID, 1010.
# 1188511880-1188511890 has one invalid ID, 1188511885.
# 222220-222224 has one invalid ID, 222222.
# 1698522-1698528 contains no invalid IDs.
# 446443-446449 has one invalid ID, 446446.
# 38593856-38593862 has one invalid ID, 38593859.
# The rest of the ranges contain no invalid IDs.





# 11-22   ---> two invalid IDs, 11 and 22.
# 95-115   ---> one invalid ID, 99
# 998-1012   --->  one invalid ID, 1010
# 1188511880-1188511890   ---> one invalid ID, 1188511885
# 222220-222224   ---> one invalid ID, 222222
# 1698522-1698528   ---> NONE (both equal and odd length)
# 446443-446449   ---> one invalid ID, 446446
# 38593856-38593862   ---> one invalid ID, 38593859
# 565653-565659   ---> NONE
# 824824821-824824827   ---> NONE
# 2121212118-2121212124   ---> NONE


input = split_lines(INPUT_FILENAME).pop()
# print(input)
# print(len(input))
arr = []
for n in input:
    ranges = n.split("-")
    if len(ranges[0]) == len(ranges[1]) and len(ranges[0]) % 2 == 1:
        continue
    arr.append(ranges)
    # print(f"{ranges[0]}\t{int(ranges[1]) - int(ranges[0])}")
# print(arr)
# print(len(arr))

total = 0
for r in arr:
    start_str, end_str = r
    start, end = int(start_str), int(end_str)
    start_str = str(start)
    if len(start_str) % 2 == 1:
        # print(f"{start}")
        start = 10 ** (len(start_str))
        if start > end:
            # print(f"{start} > {end}")
            continue
        start_str = str(start)
    curr = start
    print(f"Checking range {start}-{end}\t{end - start + 1} numbers")
    for _ in range(end - start + 1):
        print(f"  Checking {curr}")
        curr_str = str(curr)
        if len(curr_str) %2 == 1:
            break
        if curr_str[0:len(curr_str)//2] == curr_str[len(curr_str)//2:]:
            print(curr)
            total += curr
        curr += 1
print(f"Total: {total}\nExpected: {PART_ONE_EXPECTED_ANSWER}\nIs Correct: {total == PART_ONE_EXPECTED_ANSWER}")



