import numpy as np


def main():
    # filename = '13.1test.txt'
    filename = '13.1input.txt'
 
    with open(filename) as f:
        valleys = [[]]
        for line in f:
            line = line.strip()
            if line == '':
                valleys[-1] = np.array(valleys[-1])
                valleys.append([])
            else:
                valleys[-1].append(list(line))
        valleys[-1] = np.array(valleys[-1])

    mirrors = []
    for valley in valleys:
        mirror = [0, 0]
        for v in range(valley.shape[1] - 1):
            if all(all(valley[:, v - v_j] == valley[:, v + 1 + v_j]) for v_j in range(min(v + 1, valley.shape[1] - v - 1))):
                mirror[0] = v + 1
                break
        if mirror[0] == 0:
            for h in range(valley.shape[0] - 1):
                if all(all(valley[h - h_i, :] == valley[h + 1 + h_i, :]) for h_i in range(min(h + 1, valley.shape[0] - h - 1))):
                    mirror[1] = h + 1
                    break
        mirrors.append(mirror)
    print(sum(h + 100 * v for h, v in mirrors))


if __name__ == '__main__':
    main()
