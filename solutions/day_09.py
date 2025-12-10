# I hate the solution for part 2. I had wanted to stick to the standard library for all
# solutions. Part 2 of this problem is intentionally tricky, but Shapely makes it 
# extremely easy, which defeats the purpose of the challenge.
#
# I needed to complete this problem within the time limit, and the solution I was pursuing
# (ray casting algorithm) was taking too long to implement, as I was unfamiliar with it 
# before attempting this problem. So, I had to resort to using Shapely at this time.
# After the Advent of Code challenge is done, I will revisit this problem and try to 
# implement a solution (again, probably ray casting) without Shapely.
from shapely import Polygon, box

from utils.advent_day import AdventDay
from utils.process_input import split_lines_to_ints

DAY_NUMBER = 9
IS_EXAMPLE = False

def find_areas(red_tiles: list[tuple[int, int]]):
    filled_shape = Polygon(red_tiles)
    max_area = 0 # part 1
    max_area_inside_shape = 0 # part 2

    for i in range(len(red_tiles)):
        x1, y1 = red_tiles[i]
        for j in range(i + 1, len(red_tiles)):
            x2, y2 = red_tiles[j]

            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)

            area = (max_x - min_x + 1) * (max_y - min_y + 1)
            max_area = max(max_area, area) # part 1
            if filled_shape.contains(box(min_x, min_y, max_x, max_y)):
                max_area_inside_shape = max(max_area_inside_shape, area) # part 2

    return max_area, max_area_inside_shape

if __name__ == "__main__":
    advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
    red_tiles = split_lines_to_ints(advent_day.filename)
    max_area, max_area_inside_shape = find_areas(red_tiles)

    advent_day.print_both_results(
        max_area, # part 1
        max_area_inside_shape # part 2
    )