def main():
    # filename = '15.1test.txt'
    filename = '15.1input.txt'
    
    with open(filename) as f:
        sequence = f.readline().strip().split(',')

    # print(sequence)

    current_values = []
    for line in sequence:
        current_value = 0
        for char in line:
            current_value = (current_value + ord(char)) * 17 % 256
        current_values.append(current_value)
    
    # print(current_values)
    print(sum(current_values))


if __name__ == '__main__':
    main()
