from collections import Counter


filename = '7.1input.txt'
# filename = '7.1test.txt'

strength = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2')

with open(filename) as f:
    lst = [line.split() for line in f]

for i in range(len(lst)):
    hand = lst[i][0]
    hand_set = Counter(hand)
    len_hand_set = len(hand_set)

    bid = int(lst[i][1])
    lst[i][1] = bid

    if len_hand_set == 5:
        rank = [1]
    elif len_hand_set == 4:
        rank = [2]
    elif len_hand_set == 3:
        if max(hand_set.values()) == 2:
            rank = [3]
        else:
            rank = [4]
    elif len_hand_set == 2:
        if max(hand_set.values()) == 3:
            rank = [5]
        else:
            rank = [6]
    else:
        rank = [7]

    rank += [strength[::-1].index(s) for s in hand]
    lst[i][0] = rank

lst.sort()
total_winnings = sum([(i + 1) * l[1] for i, l in enumerate(lst)])
print(total_winnings)
