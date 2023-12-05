filename = '4.1input.txt'
# filename = '4.1test.txt'

numbers_you_have = []
winning_numbers = []
with open(filename) as f:
    for line in f:
        have, win = line.rstrip().split(': ')[1].split(' | ')
        numbers_you_have.append(set(int(n) for n in have.split()))
        winning_numbers.append(set(int(n) for n in win.split()))

points = 0
for i, have in enumerate(numbers_you_have):
    l = len(have & winning_numbers[i])
    if l > 0:
        points += 2 ** (l - 1)

print(numbers_you_have)
print(winning_numbers)
print(points)
