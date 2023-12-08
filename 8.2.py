import re
import itertools
import math

filename = '8.1input.txt'
# filename = '8.1test.txt'
# filename = '8.2test.txt'

with open(filename) as f:
    instructions = f.readline().strip()
    f.readline()
    network = {}
    for line in f:
        s = re.findall('\w+', line)
        network[s[0]] = (s[1], s[2])

instructions = instructions.replace('L', '0').replace('R', '1')
current = [n for n in network if n[-1] == 'A']
counters = []
for c in current:
    counter = 0
    place = c
    instructions_cycle = itertools.cycle(instructions)
    for instruction in instructions_cycle:
        if place[-1] == 'Z':
            break
        place = network[place][int(instruction)]
        counter += 1
    counters.append(counter)

print(math.lcm(*counters))
