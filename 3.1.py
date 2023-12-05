import re


def check_neighbours(x, y, l):
    x_min, x_max = max(0, x - 1), min(x + 2, len(schema))
    y_min, y_max = max(0, y - 1), min(y + l + 1, len(schema[x]))
    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            if schema[i][j] != "." and not schema[i][j].isdigit():
                return True
    return False


filename = '3.1input.txt'
# filename = '3.1test.txt'

with open(filename) as f:
    schema = [line.strip() for line in f]

numbers_xy = {}
for i, line in enumerate(schema):
    numbers_xy.update({(i, m.start(0), len(m.group(0))): int(m.group(0)) for m in re.finditer("[0-9]+", line)})

print(numbers_xy)

sum_parts = 0
for key in numbers_xy:
    if check_neighbours(*key):
        sum_parts += numbers_xy[key]

print(sum_parts)
