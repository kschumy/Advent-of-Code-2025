from pathlib import Path
from utils.part import Part

ANSWERS_DIR = "answers"
INPUT_DIR = "input"

def read_lines(input_filename: str) -> list[str]:
    data_file = _read_raw_input(input_filename)
    return [line for line in data_file.splitlines() if line.strip()]

def split_lines(input_filename: str, delimiter: str = ",") -> list[list[str]]:
    data_file = _read_raw_input(input_filename)
    return [line.split(delimiter) for line in data_file.splitlines() if line.strip()]

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