from utils.reader import read_input

# Day 01, 03
def read_lines(input_filename: str) -> list[str]:
    data_file = read_input(input_filename)
    return [line for line in data_file.splitlines() if line.strip()]

# Day 02
def split_lines(input_filename: str, delimiter: str = ",") -> list[list[str]]:
    data_file = read_input(input_filename)
    return [line.split(delimiter) for line in data_file.splitlines() if line.strip()]

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
    return ranges, values