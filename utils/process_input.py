from pathlib import Path
from utils.part import Part

ANSWERS_DIR = "answers"
INPUT_DIR = "input"

# Day 01, 03
def read_lines(input_filename: str) -> list[str]:
    data_file = _read_raw_input(input_filename)
    return [line for line in data_file.splitlines() if line.strip()]

# Day 02
def split_lines(input_filename: str, delimiter: str = ",") -> list[list[str]]:
    data_file = _read_raw_input(input_filename)
    return [line.split(delimiter) for line in data_file.splitlines() if line.strip()]

# Day 04
def read_lines_to_matrix_with_borders(
    input_filename: str,
    border_len: int = 1,
    border_char: str = ".",
) -> list[list[str]]:
    lines = _read_raw_input(input_filename).splitlines()
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

def get_expected_answer(input_filename: str, part: Part) -> str:
    answers = get_expected_answers(input_filename)
    return answers[part.value - 1]

# returns [<part one expected>, <part two expected>]
def get_expected_answers(input_filename: str) -> list[int]:
    answers_file = _read_raw(ANSWERS_DIR, input_filename)
    results = [int(line) for line in answers_file.splitlines() if line.strip()]
    if len(results) != 2:
        raise ValueError("Expected answers file must contain exactly two lines")
    return results

def _read_raw_input(input_filename: str) -> str:
    return _read_raw(INPUT_DIR, input_filename)

def _read_raw(parent_dir: str, input_filename: str) -> str:
    data_file = Path(__file__).resolve().parent.parent / parent_dir / input_filename
    return data_file.read_text()