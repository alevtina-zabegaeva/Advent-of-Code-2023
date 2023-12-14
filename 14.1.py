import numpy as np


def main():
    # filename = '14.1test.txt'
    filename = '14.1input.txt'
    
    with open(filename) as f:
        platform = [list(line.strip()) for line in f]
    platform = np.array(platform)

    max_i, max_j = platform.shape
    weights = []
    for j in range(max_j):
        lst = platform[:, j]
        o_i = np.where(lst == 'O')[0]
        for i in o_i:
            empty_i = i - 1
            while empty_i >= 0 and lst[empty_i] == '.':
                empty_i -= 1
            lst[i] = '.'
            lst[empty_i + 1] = 'O'
        platform[:, j] = lst
        o_i = np.where(lst == 'O')[0]
        weights.append(sum([max_i - o for o in o_i]))

    print(sum(weights))


if __name__ == '__main__':
    main()
