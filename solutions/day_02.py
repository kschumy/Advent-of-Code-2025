from utils.print_results import PrintResults
from utils.process_input import split_lines

DAY = "2"
INPUT_FILENAME = f"day_{str(DAY).zfill(2)}.txt"
PART_ONE_EXPECTED_ANSWER = 38158151648
PART_TWO_EXPECTED_ANSWER = 45283684555

def is_invalid_number(s: str, is_part_one: bool) -> bool:
    section_lens = []
    if is_part_one:
        if len(s) % 2 == 1:
            return False
        section_lens.append(len(s) // 2)
    else:
        for l in range(1, len(s)//2 + 1):
            if len(s) % l == 0:
                section_lens.append(l)
    
    for section_len in section_lens:
        is_invalid_number = True
        for i in range(section_len, len(s), section_len):
            if s[i:i+section_len] != s[i-section_len:i]:
                is_invalid_number = False
                break
        if is_invalid_number:
            return True
    return False

def find_sum_of_valid_numbers(arr, is_part_one: bool) -> int:
    total = 0
    for start_s, end_s in arr:
        start, end = int(start_s), int(end_s)
        for curr in range(start, end + 1):
            s = str(curr)
            if is_part_one and len(s) % 2 == 1:
                continue
            if is_invalid_number(s, is_part_one):
                total += curr
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
    for result in results:
        part, expected, actual = result
        PrintResults.print_result(DAY, part, expected, actual)