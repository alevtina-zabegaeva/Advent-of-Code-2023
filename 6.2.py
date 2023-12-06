import math


filename = '6.1input.txt'
# filename = '6.1test.txt'

with open(filename) as f:
    time =     int(''.join(c for c in f.readline() if c.isdigit()))
    distance = int(''.join(c for c in f.readline() if c.isdigit()))

print(time, distance)

t1 = math.floor((time - (time ** 2 - 4 * distance) ** 0.5) / 2)
t2 = math.ceil((time + (time ** 2 - 4 * distance) ** 0.5) / 2)
result = t2 - t1 - 1

print(result)
