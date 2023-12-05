import re


filename = '4.1input.txt'
# filename = '4.1test.txt'

numbers_you_have = []
winning_numbers = []
with open(filename) as f:
    for line in f:
        have, win = line.rstrip().split(': ')[1].split(' | ')
        numbers_you_have.append(set(int(n) for n in have.split()))
        winning_numbers.append(set(int(n) for n in win.split()))

max_card_number = len(numbers_you_have)
cards = [1] * max_card_number
for i in range(max_card_number):
    l = len(numbers_you_have[i] & winning_numbers[i])
    for j in range(i + 1, i + 1 + l):
        cards[j] += cards[i]

print(sum(cards))
