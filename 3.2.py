import re
from collections import defaultdict


def check_neighbours(x, y, l):
    x_min, x_max = max(0, x - 1), min(x + 2, len(schema))
    y_min, y_max = max(0, y - 1), min(y + l + 1, len(schema[x]))
    g = []
    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            if schema[i][j] == "*":
                g.append((i, j))
    return g


filename = '3.1input.txt'
# filename = '3.1test.txt'

with open(filename) as f:
    schema = [line.strip() for line in f]

numbers_xy = {}
for i, line in enumerate(schema):
    numbers_xy.update({(i, m.start(0), len(m.group(0))): int(m.group(0)) for m in re.finditer("[0-9]+", line)})

gears = defaultdict(list)
for key in numbers_xy:
    neighbours_gears = check_neighbours(*key)
    for gear in neighbours_gears:
        gears[gear] += [numbers_xy[key]]

sum_gear_ratio = 0
for gear, numbers in gears.items():
    if len(numbers) == 2:
        sum_gear_ratio += numbers[0] * numbers[1]

print(sum_gear_ratio)
