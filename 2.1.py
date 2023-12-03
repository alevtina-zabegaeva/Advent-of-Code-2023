filename = '2.1input.txt'
# filename = '2.1test.txt'

games = []
with open(filename) as f:
    for line in f:
        id, cubes = line.rstrip().split(': ')
        games.append([int(id[5:]), 0, 0, 0])
        cubes = cubes.split()
        for i in range(1, len(cubes), 2):
            if cubes[i][:3] == 'red':
                games[-1][1] = max(games[-1][1], int(cubes[i - 1]))
            elif cubes[i][:5] == 'green':
                games[-1][2] = max(games[-1][2], int(cubes[i - 1]))
            else:
                games[-1][3] = max(games[-1][3], int(cubes[i - 1]))

sum_id = 0
for game in games:
    if game[1] <= 12 and game[2] <= 13 and game[3] <= 14:
        sum_id += game[0]
print(sum_id)
