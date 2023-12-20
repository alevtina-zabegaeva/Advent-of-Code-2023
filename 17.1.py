import numpy as np


def main():
    # filename = '17.1test.txt'
    filename = '17.1input.txt'
    
    with open(filename) as f:
        blocks = [[int(l) for l in line.strip()] for line in f]
    blocks = np.array(blocks)
    # print(blocks)
    max_i, max_j = blocks.shape
    heat_loss_whole = sum(blocks[i, i] + blocks[i - 1, i] for i in range(max_i))

    current = {((0, 1), (0, 1), 1): blocks[0, 1],
               ((1, 0), (1, 0), 1): blocks[1, 0]}
    visited = {((0, 1), (0, 1), 1): blocks[0, 1],
               ((1, 0), (1, 0), 1): blocks[1, 0]}
    while len(current) > 0:
        current_next = {}
        for cur, heat_loss in current.items():
            cur_i, cur_j = cur[0]
            if heat_loss >= heat_loss_whole:
                continue
            if (cur_i, cur_j) == (max_i - 1, max_j - 1):
                heat_loss_whole = min(heat_loss_whole, heat_loss)
                continue
            dir_i, dir_j = cur[1]
            repeat = cur[-1]
            dir_var = [(dir_j, dir_i), (-dir_j, -dir_i)]
            if repeat != 3:
                dir_var.append((dir_i, dir_j))
            for d_i, d_j in dir_var:
                next_i, next_j = cur_i + d_i, cur_j + d_j
                repeat_next = 1
                if (d_i, d_j) == (dir_i, dir_j):
                    repeat_next += repeat
                if 0 <= next_i < max_i and 0 <= next_j < max_j:
                    if (((next_i, next_j), (d_i, d_j), repeat_next) in visited and
                        visited[((next_i, next_j), (d_i, d_j), repeat_next)] > heat_loss + blocks[next_i, next_j] or
                        not ((next_i, next_j), (d_i, d_j), repeat_next) in visited):
                        visited[((next_i, next_j), (d_i, d_j), repeat_next)] = heat_loss + blocks[next_i, next_j]
                        current_next[((next_i, next_j), (d_i, d_j), repeat_next)] = heat_loss + blocks[next_i, next_j]
        current = current_next.copy()
    print(heat_loss_whole)


if __name__ == '__main__':
    main()
