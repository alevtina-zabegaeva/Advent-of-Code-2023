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
        h_max, v_max = valley.shape
        mirror = [0, 0]
        for v in range(v_max - 1):
            length = min(v + 1, v_max - v - 1)
            counter = 0
            for v_j in range(length):
                counter += sum(valley[:, v - v_j] != valley[:, v + 1 + v_j])
                if counter > 1:
                    break
            if counter == 1:
                mirror[0] = v + 1
                break
        if mirror[0] == 0:
            for h in range(h_max - 1):
                length = min(h + 1, h_max - h - 1)
                counter = 0
                for h_i in range(length):
                    counter += sum(valley[h - h_i, :] != valley[h + 1 + h_i, :])
                    if counter > 1:
                        break
                if counter == 1:
                    mirror[1] = h + 1
                    break
        mirrors.append(mirror)

    print(sum(h + 100 * v for h, v in mirrors))


if __name__ == '__main__':
    main()
