from utils.part import Part
from utils.process_input import get_expected_answers

class AdventDay:
    def __init__(self, day: int, is_example: bool=False):
        self.day = day
        self.day_str = str(day).zfill(2)
        self.is_example = is_example

    def get_filename(self) -> str:
        return f"day_{self.day_str}{'_example' if self.is_example else ''}.txt"

    def print_both_results(self, part_one_actual: int, part_two_actual: int):
        both_parts_expected = get_expected_answers(self.get_filename())
        self._print_result(part_one_actual, both_parts_expected[0], Part.ONE)
        self._print_result(part_two_actual, both_parts_expected[1], Part.TWO)

    def print_part_result(self, actual: int, part: Part):
        if part not in [Part.ONE, Part.TWO]:
            raise ValueError(f"part must be {Part.ONE} or {Part.TWO}")
        both_parts_expected = get_expected_answers(self.get_filename())
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