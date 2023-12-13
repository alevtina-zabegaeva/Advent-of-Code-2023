def main():
    def sums(length, total_sum):
        if length == 1:
            yield (total_sum,)
        else:
            for value in range(total_sum + 1):
                for permutation in sums(length - 1, total_sum - value):
                    yield (value,) + permutation


    # filename = '12.1test.txt'
    filename = '12.1input.txt'

    map = []
    with open(filename) as f:
        for line in f:
            springs, numbers = line.strip().split()
            numbers = [int(n) for n in numbers.split(',')]
            map.append([springs, numbers])

    counter = []
    for springs, numbers in map:
        counter.append(0)
        for perm in sums(len(numbers) + 1, len(springs) - sum(numbers)):
            if any(p == 0 for p in perm[1:-1]):
                continue
            line_perm = ''.join(['.'*n + '#'*numbers[i] for i, n in enumerate(perm[:-1])] + ['.']*perm[-1])
            if all(a == b or a == '?' for a, b in zip(springs, line_perm)):
                counter[-1] += 1
    print(sum(counter))
    

if __name__ == '__main__':
    main()

