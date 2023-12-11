import numpy as np
from itertools import combinations


def main():
    # filename = '11.1test.txt'
    filename = '11.1input.txt'

    with open(filename) as f:
        universe = [list(line.strip()) for line in f]
    universe = np.array(universe)

    galaxies_i, galaxies_j = np.where(universe == '#')
    galaxies = list(zip(galaxies_i, galaxies_j))
    max_i, max_j = universe.shape
    toexpand_i = set(range(max_i)) - set(galaxies_i)
    toexpand_j = set(range(max_j)) - set(galaxies_j)

    galaxies_expanded = []
    for galaxie_i, galaxie_j in galaxies:
        galaxies_expanded.append((galaxie_i + len([1 for i in toexpand_i if galaxie_i > i]),
                                  galaxie_j + len([1 for j in toexpand_j if galaxie_j > j])))
    
    sum_distance = 0
    for pair1, pair2 in combinations(galaxies_expanded, 2):
        sum_distance += abs(pair1[0] - pair2[0]) + abs(pair1[1] - pair2[1])
    print(sum_distance)


if __name__ == '__main__':
    main()
