from collections import defaultdict
from utils.advent_day import AdventDay
from utils.process_input import read_lines_to_matrix

DAY_NUMBER = 7
IS_EXAMPLE = False # set to False for real input, or True for example input

BEAM_START_CHAR = "S"
SPLITTER = "^"

def get_split_and_timeline_counts(manifold: list[list[str]]) -> tuple[int, int]:
    beams = defaultdict(int)
    s_index = manifold[0].index(BEAM_START_CHAR) # starting position
    beams[s_index] = 1
    split_count = 0 # part 1
    for row_idx in range(1, len(manifold)):
        row = manifold[row_idx]
        new_beams = defaultdict(int)
        for col_idx, timeline_count in beams.items():
            if col_idx < 0 or col_idx >= len(row):
                continue
            if row[col_idx] == SPLITTER:
                new_beams[col_idx - 1] += timeline_count
                new_beams[col_idx + 1] += timeline_count
                split_count += 1  # count the split for part 1
            else:  # row[col_idx] is '^' or '.'
                new_beams[col_idx] += timeline_count
        beams = new_beams
    return split_count, sum(beams.values())

if __name__ == "__main__":
    advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
    lines = read_lines_to_matrix(advent_day.filename)
    split_count, total_timeline_count = get_split_and_timeline_counts(lines)
    advent_day.print_both_results(split_count, total_timeline_count)