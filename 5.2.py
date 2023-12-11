filename = '5.1input.txt'
# filename = '5.1test.txt'

with open(filename) as f:
    seeds = [int(s) for s in f.readline().split()[1:]]
    line = f.readline()
    schema = []
    schema_current = []
    flag = False
    for line in f:
        if flag:
            if line == '\n':
                schema.append(schema_current)
                schema_current = []
                flag = False
            else:
                schema_current.append([int(s) for s in line.split()])
        else:
            flag = True
    schema.append(schema_current)

seeds = [(seeds[i], seeds[i] + seeds[i +  1] - 1) for i in range(0, len(seeds), 2)]

schema_new = [{(rang[1], rang[1] + rang[2] - 1): rang[0] - rang[1] for rang in map} for map in schema]

for map in schema_new:
    seeds_old = seeds.copy()
    seeds_next = []
    while True:
        for seed in seeds:
            for rang, increment in map.items():
                if seed[0] < rang[0] <= seed[1] <= rang[1]:
                    seeds_old.remove(seed)
                    seeds_old.append((seed[0], rang[0] - 1))
                    seeds_next.append((rang[0] + increment, seed[1] + increment))
                elif rang[0] <= seed[0] <= rang[1] < seed[1]:
                    seeds_old.remove(seed)
                    seeds_old.append((rang[1] + 1, seed[1]))
                    seeds_next.append((seed[0] + increment, rang[1] + increment))
                elif rang[0] <= seed[0] and seed[1] <= rang[1]:
                    seeds_old.remove(seed)
                    seeds_next.append((seed[0] + increment, seed[1] + increment))
                elif seed[0] < rang[0] and rang[1] < seed[1]:
                    seeds_old.remove(seed)
                    seeds_old.append((seed[0], rang[0] - 1))
                    seeds_next.append((rang[0] + increment, rang[1] + increment))
                    seeds_old.append((rang[1] + 1, seed[1]))
                else:
                    continue
                break
        if set(seeds) == set(seeds_old):
            seeds = seeds_next + seeds_old
            break
        seeds = seeds_old.copy()

print(min(seeds)[0])
