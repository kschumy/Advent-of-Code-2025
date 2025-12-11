# This only includes Part 1. Solving Part 2 ended up being an integer linear programming
# problem, and my goal for the Advent of Code puzzles was not to use any external libraries
# beyond the standard library. However, implementing a solver for this proved to be far too
# time-consuming within the time constraints and spirit of the challenge.
#
# I am exploring using external libraries such as PuLP or SciPy to solve this problem after
# the challenge is over, as I find integer linear programming interesting and wish to learn
# more about it and these libraries. However, in the interest of keeping on track with the
# Advent of Code challenge, I am prioritizing completing the subsequent days first and
# tackling this problem after the challenge is complete.
from itertools import combinations

from solutions.day_08 import three_largest_circuit_sizes
from utils.advent_day import AdventDay
from utils.part import Part
from utils.process_input import read_machine_manual

DAY_NUMBER = 10
IS_EXAMPLE = True

# Part 1
def fewest_button_presses(manual):
    total_presses = 0
    for line in manual:
        light_indicators = line[0]
        buttons = line[1]
        # joltage = line[2] # presumably needed for part 2

        buttons_count = len(buttons)
        lights_count = len(light_indicators)
        target = [c == '#' for c in light_indicators]
        min_presses = buttons_count + 1

        for num_to_press in range(buttons_count + 1):
            for buttons_to_press in combinations(range(buttons_count), num_to_press):
                lights = [False] * lights_count

                for button_idx in buttons_to_press:
                    button = buttons[button_idx]
                    for light_idx in button:
                        lights[light_idx] = not lights[light_idx]
                
                if lights == target:
                    min_presses = min(min_presses, num_to_press)

        total_presses += min_presses
    return total_presses

# TODO: Part 2
# Explore solutions that use pulp or scipy (preferably pulp?)

if __name__ == "__main__":
    advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
    manual = read_machine_manual(advent_day.filename)
    total_presses = fewest_button_presses(manual)
    
    # Replace with printing both results when part 2 is implemented
    advent_day.print_part_result(total_presses, Part.ONE)
    # advent_day.print_both_results(
    #     total_presses, # Part 1
    #     "Part 2 not yet implemented", # Part 2
    # )