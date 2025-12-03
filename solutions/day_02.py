from utils.process_input import split_lines
## Example input from question prompt
# INPUT_FILENAME = "day_02_example.txt"
# PART_ONE_EXPECTED_ANSWER = 1227775554
# PART_TWO_EXPECTED_ANSWER = 4174379265

INPUT_FILENAME = "day_02.txt"
PART_ONE_EXPECTED_ANSWER = 38158151648
PART_TWO_EXPECTED_ANSWER = 45283684555

def find_sum_of_valid_numbers(arr, is_part_one: bool) -> int:
    total = 0
    for r in arr:
        start_str, end_str = r
        start, end = int(start_str), int(end_str)
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

    return total

if __name__ == "__main__":
    input = split_lines(INPUT_FILENAME).pop()
    part_one_arr = []
    part_two_arr = []
    for n in input:
        ranges = n.split("-")
        if not (len(ranges[0]) == len(ranges[1]) and len(ranges[0]) % 2 == 1):
            part_one_arr.append(ranges)
        part_two_arr.append(ranges)


    results = [
        ("ONE", PART_ONE_EXPECTED_ANSWER, find_sum_of_valid_numbers(part_one_arr, True)),
        ("TWO", PART_TWO_EXPECTED_ANSWER, find_sum_of_valid_numbers(part_two_arr, False)),
    ]
    for name, expected, actual in results:
        print(
            f"PART {name} ANSWER:\n"
            f"\tExpected: {expected}\n"
            f"\tActual:   {actual}\n"
            f"\tIs Correct: {expected == actual}\n"
        )
# if is_part_one:
#     print(f"Total: {total}\nExpected: {PART_ONE_EXPECTED_ANSWER}\nIs Correct: {total == PART_ONE_EXPECTED_ANSWER}\nDiff: {PART_ONE_EXPECTED_ANSWER - total}")
# else:
#     print(f"Total: {total}\nExpected: {PART_TWO_EXPECTED_ANSWER}\nIs Correct: {total == PART_TWO_EXPECTED_ANSWER}\nDiff: {PART_TWO_EXPECTED_ANSWER - total}")


