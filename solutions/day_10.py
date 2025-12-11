
from utils.advent_day import AdventDay
from utils.process_input import read_machine_manual

DAY_NUMBER = 10
IS_EXAMPLE = True

advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
# brackets_arr, button_sets, joltage_set
manual = read_machine_manual(advent_day.filename)
print(f"manual: {manual}")
print(f"brackets_arr: {manual[0][0]}") # brackets_arr: ['.', '#', '#', '.']
print(f"button_sets: {manual[0][1]}") # button_sets: [{3}, {1, 3}, {2}, {2, 3}, {0, 2}, {0, 1}]
# print(f"joltage_set: {manual[0][2]}")

from itertools import combinations

total_presses = 0

for line in manual:
    # brackets = line[0]
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


# ABANDONED THIS APPROACH FOR NOW - it goes off the rails
# for line in manual:
#     brackets = line[0]
#     buttons = line[1]
#     # joltage = line[2]
    
#     need_indexes = set()
#     for i in range(len(brackets)):
#         if brackets[i] == '#':
#             need_indexes.add(i)

#     need_index_to_button_indexes = {}
#     un_needed_indexes_to_button_indexes = {} # not used but might be helpful later?
#     for i in range(len(buttons)):
#         button = buttons[i]
#         for button_index in button:
#             if button_index not in need_index_to_button_indexes:
#                 need_index_to_button_indexes[button_index] = set()
#             need_index_to_button_indexes[button_index].add(i)
#     print(f"need_index_to_button_indexes: {need_index_to_button_indexes}")