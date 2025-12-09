from collections import defaultdict
import math
from utils.advent_day import AdventDay
from utils.process_input import split_lines_to_ints
from utils.union_find import UnionFind

DAY_NUMBER = 8
IS_EXAMPLE = False # set to False for real input, or True for example input

NUM_OF_CONNECTIONS = 10 if IS_EXAMPLE else 1000 # from problem statement

advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)


positions = split_lines_to_ints(advent_day.filename)
# print(positions)

edges = []
for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
        dist = math.dist(positions[i], positions[j])
        edges.append((dist, i, j))
edges.sort()
# print(edges)

uf = UnionFind(len(positions))
for k in range(NUM_OF_CONNECTIONS):
    _, pos_1, pos_2 = edges[k]
    uf.union(pos_1, pos_2)

curcuits = defaultdict(int)
for l in range(len(positions)):
    root = uf.find(l)
    curcuits[root] += 1

sizes = sorted(curcuits.values(), reverse=True)
print(sizes[0] * sizes[1] * sizes[2])

print(42840)