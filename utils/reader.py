from pathlib import Path

ANSWERS_DIR = "answers"
INPUT_DIR = "input"

def read_input(input_filename: str) -> str:
    return _read_raw(INPUT_DIR, input_filename)

def read_answers(input_filename: str) -> str:
    return _read_raw(ANSWERS_DIR, input_filename)

def _read_raw(parent_dir: str, input_filename: str) -> str:
    data_file = Path(__file__).resolve().parent.parent / parent_dir / input_filename
    return data_file.read_text()