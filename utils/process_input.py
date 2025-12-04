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
def read_lines_to_matrix_with_borders(
    input_filename: str,
    border_len: int = 1,
    border_char: str = ".",
) -> list[list[str]]:
    lines = read_input(input_filename).splitlines()
    border_row = [border_char] * (len(lines[0]) + 2 * border_len)
    padding = [border_char] * border_len
    arr = []

    # top border
    for _ in range(border_len):
        arr.append(border_row.copy())

    # middle rows with border on sides
    for line in lines:
        arr.append(padding + list(line) + padding)

    # bottom border
    for _ in range(border_len):
        arr.append(border_row.copy())

    return arr