from itertools import combinations

from utils.advent_day import AdventDay
from utils.process_input import read_machine_manual

DAY_NUMBER = 10
IS_EXAMPLE = True

advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
manual = read_machine_manual(advent_day.filename)

### Part 1 ###
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
    print(f"min_presses: {min_presses} for line: {light_indicators} with buttons: {buttons}")

print(f"Total: {total_presses}")
### END PART 1 ###