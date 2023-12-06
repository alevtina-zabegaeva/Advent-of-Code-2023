import math


filename = '6.1input.txt'
# filename = '6.1test.txt'

with open(filename) as f:
    times =     [int(s) for s in f.readline()[9:].split()]
    distances = [int(s) for s in f.readline()[9:].split()]

result = 1
for i, time in enumerate(times):
    t1 = math.floor((time - (time ** 2 - 4 * distances[i]) ** 0.5) / 2)
    t2 = math.ceil((time + (time ** 2 - 4 * distances[i]) ** 0.5) / 2)
    print(t2, t1, t2 - t1 - 1)
    result *= t2 - t1 - 1

print(result)
