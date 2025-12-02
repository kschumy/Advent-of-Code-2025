from pathlib import Path

def read_lines(input_filename: str):
    data_file = Path(__file__).resolve().parent.parent / "input" / input_filename
    return [line for line in data_file.read_text().splitlines() if line.strip()]