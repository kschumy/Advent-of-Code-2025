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
        _, pos_1, pos_2 = edges[i]
        uf.union(pos_1, pos_2)
        
        circuits = defaultdict(int)
        for j in range(len(positions)):
            root = uf.find(j)
            circuits[root] += 1

    return prod(sorted(circuits.values())[-3:])


# PART 2
def get_distance_from_wall(positions, edges):
    uf = UnionFind(len(positions))
    for k in range(NUM_OF_CONNECTIONS):
        _, pos_1, pos_2 = edges[k]
        uf.union(pos_1, pos_2)

    for k in range(len(edges)):
        _, pos_1, pos_2 = edges[k]
        uf.union(pos_1, pos_2)

        root = uf.find(0)
        is_all_unified = True
        for i in range(len(positions)):
            if uf.find(i) != root:
                is_all_unified = False
                break
        
        if is_all_unified:
            return positions[pos_1][0] * positions[pos_2][0]



if __name__ == "__main__":
    advent_day = AdventDay(DAY_NUMBER, IS_EXAMPLE)
    positions = split_lines_to_ints(advent_day.filename)
    edges = get_edges(positions)
    advent_day.print_both_results(
        three_largest_circuit_sizes(positions, edges),
        get_distance_from_wall(positions, edges),
    )