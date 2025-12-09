from collections import defaultdict
from math import dist, prod

from utils.advent_day import AdventDay
from utils.process_input import split_lines_to_ints
from utils.union_find import UnionFind

DAY_NUMBER = 8
IS_EXAMPLE = False # set to False for real input, or True for example input

NUM_OF_CONNECTIONS = 10 if IS_EXAMPLE else 1000 # from problem statement

def get_edges(positions):
    edges = []
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            distance = dist(positions[i], positions[j])
            edges.append((distance, i, j))
    edges.sort()
    return edges

# PART 1
def three_largest_circuit_sizes(positions, edges):
    uf = UnionFind(len(positions))
    for i in range(NUM_OF_CONNECTIONS):
        _, idx_1, idx_2 = edges[i]
        uf.union(idx_1, idx_2)

    circuits = defaultdict(int)
    for j in range(len(positions)):
        root = uf.find(j)
        circuits[root] += 1
    
    return prod(sorted(circuits.values(), reverse=True)[:3])


# PART 2
def get_distance_from_wall(positions, edges):
    uf = UnionFind(len(positions))
    for _, idx_1, idx_2 in edges:
        uf.union(idx_1, idx_2)
        if uf.is_unified():
            return positions[idx_1][0] * positions[idx_2][0]

if __name__ == "__main__":
    advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
    positions = split_lines_to_ints(advent_day.filename)
    edges = get_edges(positions)
   
    advent_day.print_both_results(
        three_largest_circuit_sizes(positions, edges), # PART 1
        get_distance_from_wall(positions, edges), # PART 2
    )