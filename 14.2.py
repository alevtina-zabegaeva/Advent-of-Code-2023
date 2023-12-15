import numpy as np


def main():
    def tilt_north(platform):
        plat = platform.copy()
        max_j = plat.shape[1]
        for j in range(max_j):
            lst = plat[:, j]
            o_i = np.where(lst == 'O')[0]
            for i in o_i:
                empty_i = i - 1
                while empty_i >= 0 and lst[empty_i] == '.':
                    empty_i -= 1
                lst[i] = '.'
                lst[empty_i + 1] = 'O'
            plat[:, j] = lst
        return plat


    def tilt_cycle(platform):
        plat = platform.copy()

        plat = tilt_north(plat)

        plat = np.rot90(plat, k=-1)
        plat = tilt_north(plat)
        plat = np.rot90(plat, k=1)

        plat = np.flipud(plat)
        plat = tilt_north(plat)
        plat = np.flipud(plat)

        plat = np.rot90(plat, k=1)
        plat = tilt_north(plat)
        plat = np.rot90(plat, k=-1)
        return plat


    def find_period(lst):
        max_len = 50
        start = 0
        for start in range(len(lst) // 2):
            for period in range(1, max_len + 1):
                if all([lst[start: start + period] == lst[start + period * i: start + period * (i + 1)] for i in range(1, (len(lst) - start) // period - 1)]):
                    return start, period
        return -1, -1


    # filename = '14.1test.txt'
    filename = '14.1input.txt'
    cycles = 400
    cycles_max = 1000000000

    with open(filename) as f:
        platform = [list(line.strip()) for line in f]
    platform = np.array(platform)

    max_i, max_j = platform.shape
    weights = []
    for k in range(cycles):
        platform = tilt_cycle(platform)
        o_i = np.where(platform == 'O')[0]
        weights.append(sum([max_i - o for o in o_i]))

    start, period = find_period(weights)
    print(weights[cycles_max - 1 - (cycles_max - 1 - start) // period * period])


if __name__ == '__main__':
    main()
