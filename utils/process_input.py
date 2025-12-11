import re

from utils.reader import read_input

# Day 01, 03
def read_lines(input_filename: str) -> list[str]:
    data_file = read_input(input_filename)
    return [line for line in data_file.splitlines() if line.strip()]

# Day 02
def split_lines(input_filename: str, delimiter: str = ",") -> list[list[str]]:
    data_file = read_input(input_filename)
    return [line.split(delimiter) for line in data_file.splitlines() if line.strip()]

# Day 08, 09
def split_lines_to_ints(input_filename: str, delimiter: str = ",") -> list[list[int]]:
    data_file = read_input(input_filename)
    return [list(map(int, line.split(delimiter))) for line in data_file.splitlines() if line.strip()]

# Day 07
def read_lines_to_matrix(input_filename: str) -> list[list[str]]:
    lines = read_input(input_filename).splitlines()
    return [list(line) for line in lines]

# Day 04
def read_lines_to_matrix_with_borders(input_filename: str, border_char: str = ".") -> list[list[str]]:
    lines = read_input(input_filename).splitlines()
    border_row = [border_char] * (len(lines[0]) + 2)
    arr = []
    arr.append(border_row.copy()) # top border
    for line in lines:
        arr.append([border_char] + list(line) + [border_char]) # middle rows with border on each side
    arr.append(border_row.copy()) # bottom border
    return arr

# Day 05
def read_input_with_ranges_and_integers(input_filename: str) -> tuple[list[list[int]], list[int]]:
    ranges_lines, values_lines = read_input(input_filename).strip().split('\n\n', 1)
    ranges = []
    for line in ranges_lines.splitlines():
        start_str, end_str = line.split("-")
        ranges.append([int(start_str), int(end_str)])
    values = []
    for line in values_lines.splitlines():
        values.append(int(line))
    return (ranges, values)

# Day 06 - part 1
# All lines except last line contain space-separated integers
# Last line contains space-separated strings
def read_lines_with_numbers_and_strings(input_filename: str) -> tuple[list[list[int]], list[str]]:
    data_lines = read_input(input_filename).splitlines()
    strs = data_lines.pop().split()
    numbers = [list(map(int, line.split())) for line in data_lines]
    return (numbers, strs)

# Day 06 - part 2
def read_lines_with_last_line_removed(input_filename: str) -> list[str]:
    return read_input(input_filename).splitlines()[:-1]

# Day 10
# Example line: [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
def read_machine_manual(input_filename: str):
    data_lines = read_input(input_filename).splitlines()
    manual = []
    for line in data_lines:
        brackets = re.search(r'\[([.#]+)\]', line).group(1)
        
        button_matches = re.findall(r'\(([0-9,]+)\)', line)
        buttons = [set(map(int, match.split(','))) for match in button_matches]
        
        joltage_match = re.search(r'\{([0-9,]+)\}', line)
        joltage = set(map(int, joltage_match.group(1).split(','))) if joltage_match else set()

        manual.append((brackets, buttons, joltage))
    return manual