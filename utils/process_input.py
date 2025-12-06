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
def read_input_with_ranges_and_integers(input_filename: str) -> tuple[list[list[int, int]], list[int]]:
    lines = read_input(input_filename).splitlines()
    end_line_index = lines.index('')
    ranges = []
    for i in range(0, end_line_index):
        range_str = lines[i].split("-")
        ranges.append([int(range_str[0]), int(range_str[1])])
    values = []
    for i in range(end_line_index + 1, len(lines)):
        values.append(int(lines[i]))
    return ranges, values