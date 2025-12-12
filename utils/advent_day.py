from utils.part import Part
from utils.reader import read_answers

class AdventDay:
    def __init__(self, day: int, is_example: bool=False):
        self.day = day
        self.day_str = str(day).zfill(2)
        self.is_example = is_example
        self.filename = f"day_{self.day_str}{'_example' if self.is_example else ''}.txt"

    def get_expected_answer(self, input_filename: str, part: Part) -> str:
        answers = self.get_expected_answers(input_filename)
        return answers[part.value - 1]

    # returns [<part one expected>, <part two expected>]
    def get_expected_answers(self, input_filename: str) -> list[int]:
        answers_file = read_answers(input_filename)
        results = [int(line) for line in answers_file.splitlines() if line.strip()]
        if len(results) != 2:
            raise ValueError("Expected answers file must contain exactly two lines")
        return results
    
    # FIXME: temp bandaid for day 11 to deal with different example input
    def get_filename(self, only_part: Part=None):
        if only_part:
            only_filename, file_extension = self.filename.split(".")
            return f"{only_filename}_part_{only_part}.{file_extension}"
        else:
            return self.filename

    def print_both_results(self, part_one_actual: int, part_two_actual: int):
        both_parts_expected = self.get_expected_answers(self.filename)
        self._print_result(part_one_actual, both_parts_expected[0], Part.ONE)
        self._print_result(part_two_actual, both_parts_expected[1], Part.TWO)

    def print_part_result(self, actual: int, part: Part):
        if part not in [Part.ONE, Part.TWO]:
            raise ValueError(f"part must be {Part.ONE} or {Part.TWO}")
        both_parts_expected = self.get_expected_answers(self.filename)
        self._print_result(actual, both_parts_expected[part.value - 1], part)

    def _print_result(self, actual: int, expected: int, part: Part):
        difference = expected - actual
        is_correct = not difference
        print(
            f"\nDAY {self.day}, PART {part.value} ANSWER:\n"
            f"\tExpected: {expected}\n"
            f"\tActual:   {actual}\n"
            f"\tIs Correct? {"✅" if is_correct else "❌\tDiff: " + str(difference)}\n"
        )