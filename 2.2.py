filename = '2.1input.txt'
# filename = '2.1test.txt'

games = []
with open(filename) as f:
    for line in f:
        _, cubes = line.rstrip().split(': ')
        games.append([0, 0, 0])
        cubes = cubes.split()
        for i in range(1, len(cubes), 2):
            if cubes[i][:3] == 'red':
                games[-1][0] = max(games[-1][0], int(cubes[i - 1]))
            elif cubes[i][:5] == 'green':
                games[-1][1] = max(games[-1][1], int(cubes[i - 1]))
            else:
                games[-1][2] = max(games[-1][2], int(cubes[i - 1]))

sum_power = sum([game[0]*game[1]*game[2] for game in games])
print(sum_power)
