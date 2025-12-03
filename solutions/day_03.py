from utils.process_input import read_lines

# INPUT_FILENAME = "day_03_example.txt"
# PART_ONE_EXPECTED_ANSWER = 357
# PART_TWO_EXPECTED_ANSWER = 3121910778619

# INPUT_FILENAME = "day_03.txt"
# PART_ONE_EXPECTED_ANSWER = 17324
# PART_TWO_EXPECTED_ANSWER = 6498



    # In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
    # In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
    # In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
    # In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.


## PART ONE SOLUTION ###
lines = read_lines(INPUT_FILENAME)
# print(lines)
total = 0
for line in lines:
    curr_total = [line[0], line[1]]
    # print(curr_total)
    for i in range(1, len(line) - 1):
        if line[i] > curr_total[0]:
            curr_total = [line[i], line[i + 1]]
        elif line[i] > curr_total[1]:
            curr_total[1] = line[i]
    curr_total[1] = max(curr_total[1], line[-1])
    total += int("".join(curr_total))
print(total)
## END PART ONE SOLUTION ###


# DIGIT_SPAN = 12
# lines = read_lines(INPUT_FILENAME)
# # # print(lines)
# total = 0
# for line in lines:
#     curr = list(line[len(line) - DIGIT_SPAN:])
#     print(curr)
    
    
#     # for i in range(DIGIT_SPAN, len(line)):
#     #     num_str = line[i]
#     #     for j in range(DIGIT_SPAN):
#     #         if num_str > curr[j]:
#     #             curr = curr[0:j] + 
