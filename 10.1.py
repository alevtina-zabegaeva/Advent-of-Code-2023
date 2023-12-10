import numpy as np

def main():
    # filename = '10.1test.txt'
    # filename = '10.2test.txt'
    filename = '10.1input.txt'

    with open(filename) as f:
        map = [list(line.strip()) for line in f]
    map = np.array(map)
    map[map == '7'] = 'T'
    print(map)

    connection = {
        (0, 1):  ('-', 'T', 'J'),  # ->
        (0, -1): ('-', 'L', 'F'),  # <-
        (1, 0):  ('|', 'J', 'L'),  # down
        (-1, 0): ('|', 'T', 'F')   # up
    }
    direction = {
        '-': ((0, 1), (0, -1)),
        '|': ((1, 0), (-1, 0)),
        'T': ((0, -1), (1, 0)),
        'J': ((-1, 0), (0, -1)),
        'L': ((-1, 0), (0, 1)),
        'F': ((1, 0), (0, 1))
    }

    current_ij = np.where(map == 'S')
    current_ij = [(current_ij[0][0], current_ij[1][0])]
    print()

    counter = 0
    next_ij = set()
    for r_i, r_j in connection:
        if map[current_ij[0][0] + r_i, current_ij[0][1] + r_j] in connection[(r_i, r_j)]:
            next_ij.add((current_ij[0][0] + r_i, current_ij[0][1] + r_j))

    while len(next_ij) > 0:
        nextnext_ij = set()
        for c_ij in current_ij:
            map[c_ij] = counter
        for n_i, n_j in next_ij:
            for d_i, d_j in direction[map[n_i, n_j]]:
                if map[n_i + d_i, n_j + d_j] in direction:
                    nextnext_ij.add((n_i + d_i, n_j + d_j))
        current_ij = next_ij.copy()
        next_ij = nextnext_ij.copy()
        counter += 1
    for c_ij in current_ij:
        map[c_ij] = counter
    print(map)
    print(counter)


if __name__ == '__main__':
    main()
