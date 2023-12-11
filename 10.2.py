import numpy as np

def main():
    # filename = '10.1test.txt'
    # filename = '10.2test.txt'
    filename = '10.1input.txt'

    with open(filename) as f:
        pipe_map = [list(line.strip()) for line in f]
    pipe_map = np.array(pipe_map)
    pipe_map[pipe_map == '7'] = 'T'

    connection = {
        (0, 1):  ('-', 'T', 'J'),  # ->
        (0, -1): ('-', 'L', 'F'),  # <-
        (1, 0):  ('|', 'J', 'L'),  # down
        (-1, 0): ('|', 'T', 'F')   # up
    }
    direction = {
        '-': {(0, 1), (0, -1)},
        '|': {(1, 0), (-1, 0)},
        'T': {(0, -1), (1, 0)},
        'J': {(-1, 0), (0, -1)},
        'L': {(-1, 0), (0, 1)},
        'F': {(1, 0), (0, 1)}
    }

    map = pipe_map.copy()
    current_ij = np.where(map == 'S')
    current_ij = [(current_ij[0][0], current_ij[1][0])]

    counter = 0
    next_ij = set()
    start_pipe = set()
    for r_i, r_j in connection:
        if map[current_ij[0][0] + r_i, current_ij[0][1] + r_j] in connection[(r_i, r_j)]:
            next_ij.add((current_ij[0][0] + r_i, current_ij[0][1] + r_j))
            start_pipe.add((r_i, r_j))
    for key, value in direction.items():
        if start_pipe == value:
            start_pipe = key
            break
    pipe_map[current_ij[0][0], current_ij[0][1]] = start_pipe
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
    pipe_map[pipe_map == map] = '.'
    print(pipe_map)

    counter = 0
    for line in pipe_map:
        pipe_counter = 0
        last_turn = ''
        for l in line:
            if (l == '|' or
                l == 'J' and last_turn == 'F' or
                l == 'T' and last_turn == 'L'):
                pipe_counter += 1
            elif l == 'F' or l == 'L':
                last_turn = l
            elif l == '.' and pipe_counter % 2 == 1:
                counter += 1
    print(counter)

if __name__ == '__main__':
    main()
