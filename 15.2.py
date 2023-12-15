import regex as re


def main():
    def hash(line):
        current_value = 0
        for char in line:
            current_value = (current_value + ord(char)) * 17 % 256
        return current_value


    # filename = '15.1test.txt'
    filename = '15.1input.txt'
    
    with open(filename) as f:
        sequence = f.readline().strip().split(',')

    boxes = [[] for _ in range(256)]

    for line in sequence:
        label = re.search('[a-zA-Z]+', line).group()
        box = hash(label)
        if line[-1] == '-':
            for i, l in enumerate(boxes[box]):
                if l[0] == label:
                    boxes[box].pop(i)
                    break
        else:
            focal = int(line[-1])
            for i, l in enumerate(boxes[box]):
                if l[0] == label:
                    boxes[box][i][1] = focal
                    break
            else:
                boxes[box].append([label, focal])

    focusing_power = []    
    for i, box in enumerate(boxes):
        if len(box) > 0:
            for j, lens in enumerate(box):
                focusing_power.append((i + 1) * (j + 1) * lens[1])
    print(sum(focusing_power))
    

if __name__ == '__main__':
    main()
