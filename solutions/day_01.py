from utils.process_input import read_lines

# L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82

#     The dial starts by pointing at 50.
#     The dial is rotated L68 to point at 82.
#     The dial is rotated L30 to point at 52.
#     The dial is rotated R48 to point at 0.
#     The dial is rotated L5 to point at 95.
#     The dial is rotated R60 to point at 55.
#     The dial is rotated L55 to point at 0.
#     The dial is rotated L1 to point at 99.
#     The dial is rotated L99 to point at 0.
#     The dial is rotated R14 to point at 14.
#     The dial is rotated L82 to point at 32.
#
# Because the dial points at 0 a total of three times 
# during this process, the password in this example is 3.

START_NUM = 50
MAX_NUM = 99
MIN_NUM = 0
ROTATION_AMOUNT = MAX_NUM + 1  # 0-99 inclusive

LEFT = "L"
RIGHT = "R"

curr_num = START_NUM

lines = read_lines("day_01.txt")
# print("lines:", len(lines))

passed_zero_count = 0
for line in lines:
    direction = line[0]
    amount = int(line[1:])
    
    passed_zero_count += amount // ROTATION_AMOUNT
    amount %= ROTATION_AMOUNT
    # print(f"{line}\t{amount}")
    if amount == 0:
        amount = ROTATION_AMOUNT
    if direction == LEFT:
        if curr_num > amount:
            # print(f"{line}\t{amount}\t{curr_num}")
            curr_num -= amount
        else:
            if curr_num != 0:
                passed_zero_count += 1
            beyond_zero = amount - curr_num
            curr_num = MAX_NUM - beyond_zero + 1
            if curr_num > MAX_NUM:
                curr_num = 0
    else:
        if curr_num + amount <= MAX_NUM:
            curr_num += amount
        else:
            if curr_num != 0:
                passed_zero_count += 1
            beyond_zero = curr_num + amount
            # print(beyond_zero)
            curr_num = (MAX_NUM - beyond_zero + 1) * -1
    # if curr_num == 0:
    #     passed_zero_count += 1
    print(f"--- \t{line}\t{curr_num}\t{passed_zero_count}")

print(f"\n-----\n{passed_zero_count}\n")