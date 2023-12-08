import re
import itertools


filename = '8.1input.txt'
# filename = '8.1test.txt'

with open(filename) as f:
    instructions = f.readline().strip()
    f.readline()
    network = {}
    for line in f:
        s = re.findall('\w+', line)
        network[s[0]] = (s[1], s[2])

instructions = itertools.cycle(instructions.replace('L', '0').replace('R', '1'))

current = 'AAA'
counter = 0
for instruction in instructions:
    if current == 'ZZZ':
        break
    current = network[current][int(instruction)]
    counter += 1

print(counter)
