from utils.process_input import read_lines

INPUT_FILENAME = "day_03.txt"
PART_ONE_EXPECTED_ANSWER = 17324
PART_TWO_EXPECTED_ANSWER = 171846613143331

PART_ONE_DIGIT_SPAN = 2
PART_TWO_DIGIT_SPAN = 12

def largest_possible_joltage(s: str, digit_span: int) -> int:
    n = len(s)
    stack = []
    for i, ch in enumerate(s):
        while stack and ch > stack[-1] and len(stack) + (n - i) > digit_span:
            stack.pop()
        if len(stack) < digit_span:
            stack.append(ch)
    return int(''.join(stack[:digit_span]))

def get_total_voltage(lines, digit_span):
    total = 0
    for line in lines:
        total += largest_possible_joltage(line, digit_span)
    return total

if __name__ == "__main__":
    lines = read_lines(INPUT_FILENAME)
    results = [
        ("ONE", PART_ONE_EXPECTED_ANSWER, get_total_voltage(lines, PART_ONE_DIGIT_SPAN)),
        ("TWO", PART_TWO_EXPECTED_ANSWER, get_total_voltage(lines, PART_TWO_DIGIT_SPAN)),
    ]
    for name, expected, actual in results:
        print(
            f"PART {name} ANSWER:\n"
            f"\tExpected: {expected}\n"
            f"\tActual:   {actual}\n"
            f"\tIs Correct: {expected == actual}\n"
        )
