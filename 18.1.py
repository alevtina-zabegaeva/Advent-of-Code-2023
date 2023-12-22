def main():
    # filename = '18.1test.txt'
    filename = '18.1input.txt'
    
    plan = []
    with open(filename) as f:
        for line in f:
            d, n, _ = line.strip().split()
            plan.append((d, int(n)))

    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    trench = {(0, 0)}
    current = (0, 0)
    for dir, length in plan:
        dir_i, dir_j = directions[dir]
        for _ in range(1, length + 1):
            current = (current[0] + dir_i, current[1] + dir_j)
            trench.add(current)

    min_i = min(trench)[0]
    current = [t for t in trench if t[0] == min_i + 1]
    current = {(min_i + 1, (current[0][1] + current[1][1]) // 2)}
    interior = current.copy()
    while len(current) > 0:
        current_next = set()
        for cur_i, cur_j in current:
            for dir_i, dir_j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                next_i, next_j = cur_i + dir_i, cur_j + dir_j
                if not (next_i, next_j) in trench:
                    if not (next_i, next_j) in interior:
                        current_next.add((next_i, next_j))
                    interior.add((next_i, next_j))
        current = current_next.copy()

    print(len(interior) + len(trench))

   
if __name__ == '__main__':
    main()
