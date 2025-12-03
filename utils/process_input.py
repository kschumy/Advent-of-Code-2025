from pathlib import Path

def read_lines(input_filename: str):
    data_file = _read_raw(input_filename)
    return [line for line in data_file.splitlines() if line.strip()]

def split_lines(input_filename: str, delimiter: str = ","):
    data_file = _read_raw(input_filename)
    return [line.split(delimiter) for line in data_file.splitlines() if line.strip()]

def _read_raw(input_filename: str):
    data_file = Path(__file__).resolve().parent.parent / "input" / input_filename
    return data_file.read_text()