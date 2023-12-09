filename = '9.1input.txt'
# filename = '9.1test.txt'

with open(filename) as f:
    history = [list(map(int, s.split())) for s in f]

result = 0
for lst in history:
    lst_lst = [lst.copy()]
    while not all(l == 0 for l in lst_lst[-1]):
        lst_lst.append([lst_lst[-1][i] - lst_lst[-1][i - 1] for i in range(1, len(lst_lst[-1]))])
    for i in range(len(lst_lst) - 1, 0, -1):
        lst_lst[i - 1].append(lst_lst[i - 1][-1] + lst_lst[i][-1])
    result += lst_lst[0][-1]

print(result)
