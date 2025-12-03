from utils.process_input import split_lines
## Example input from question prompt
INPUT_FILENAME = "day_02_example.txt"
# PART_ONE_EXPECTED_ANSWER = 
# PART_TWO_EXPECTED_ANSWER = 

# 
# INPUT_FILENAME = "day_02.txt"
# PART_ONE_EXPECTED_ANSWER = 
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


input = split_lines(INPUT_FILENAME)
print(input)
arr = []
for n in input:
    ranges = n.split("-")
    if len(ranges[0]) == len(ranges[1]) and len(ranges[0]) % 2 == 1:
        continue
    arr.append(ranges)

