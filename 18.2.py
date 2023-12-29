def main():
    # filename = '18.1test.txt'
    filename = '18.1input.txt'
    
    plan = []
    with open(filename) as f:
        for line in f:
            _, _, n = line.strip().split()
            plan.append((n[-2], int(n[2:-2], 16)))

    directions = {'3': (-1, 0), '1': (1, 0), '2': (0, -1), '0': (0, 1)}
    trench = [(0, 0)]
    current = (0, 0)
    for dir, length in plan:
        dir_i, dir_j = directions[dir]
        current = (current[0] + dir_i*length, current[1] + dir_j*length)
        trench.append(current)

    n = len(trench)
    trench_len = sum(abs(trench[i + 1][0]  - trench[i][0] + trench[i + 1][1] - trench[i][1]) for i in range(n - 1)) // 2 + 1
    trench.append(trench[1])

    interior = abs(sum(trench[i][0] * (trench[i + 1][1] - trench[i - 1][1]) for i in range(1, n))) // 2
    print(interior + trench_len)

   
if __name__ == '__main__':
    main()
