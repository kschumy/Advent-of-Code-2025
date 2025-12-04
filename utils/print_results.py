class PrintResults:
    @staticmethod
    def print_result(day, part, expected, actual):
        print(
            f"\nDAY {day}, PART {part} SOLUTION:\n"
            f"\tExpected: {expected}\n"
            f"\tActual:   {actual}\n"
            f"\tIs Correct?: {expected == actual}\n"
        )
