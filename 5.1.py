filename = '5.1input.txt'
# filename = '5.1test.txt'

calibration_value = 0
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

l = len(seeds)
for map in schema:
    for j in range(l):
        for rang in map:
            if rang[1] <= seeds[j] < rang[1] + rang[2]:
                seeds[j] = rang[0] + seeds[j] - rang[1]
                break

print(min(seeds))
