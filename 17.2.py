import numpy as np


def main():
    # filename = '17.1test.txt'
    filename = '17.1input.txt'
    
    with open(filename) as f:
        blocks = [[int(l) for l in line.strip()] for line in f]
    blocks = np.array(blocks)

    max_i, max_j = blocks.shape
    max_i_x4 = ((max_i - 1) // 4 - 1) * 4
    heat_loss_whole = 0
    for i in range(0, max_i_x4 + 1, 4):
        heat_loss_whole += sum(blocks[i, i + 1: i + 5]) + sum(blocks[i + 1: i + 5, i + 4])
    heat_loss_whole += sum(blocks[max_i_x4, max_i_x4 + 1: max_i]) + sum(blocks[max_i_x4 + 1: max_i, max_j - 1])

    current = {((0, 0), (0, 1)): 0,
               ((0, 0), (1, 0)): 0}
    visited = current.copy()
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
            for repeat in range(4, 11):
                next_i, next_j = cur_i + repeat * dir_i, cur_j + repeat * dir_j
                if 0 <= next_i < max_i and 0 <= next_j < max_j:
                    heat_next = sum([blocks[cur_i + r * dir_i, cur_j + r * dir_j] for r in range(1, repeat + 1)])
                    for d_i, d_j in ((dir_j, dir_i), (-dir_j, -dir_i)):
                        if (((next_i, next_j), (d_i, d_j)) in visited and
                            visited[((next_i, next_j), (d_i, d_j))] > heat_loss + heat_next or
                            not ((next_i, next_j), (d_i, d_j)) in visited):
                            visited[((next_i, next_j), (d_i, d_j))] = heat_loss + heat_next
                            current_next[((next_i, next_j), (d_i, d_j))] = heat_loss + heat_next
        current = current_next.copy()

    print(heat_loss_whole)


if __name__ == '__main__':
    main()
