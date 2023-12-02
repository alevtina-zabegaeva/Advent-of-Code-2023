import re

def make_number(n):
    if n.isdigit():
        return int(n)
    return names_to_numbers[n]


filename = '1.1input.txt'
# filename = '1.2test.txt'
# filename = 'day01.txt'

digits = r'[0-9]|one|two|three|four|five|six|seven|eight|nine'
digits_reversed = r'[0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin'
names_to_numbers = {
    'one': 1, 'eno': 1,
    'two': 2, 'owt': 2,
    'three': 3, 'eerht': 3,
    'four': 4, 'ruof': 4,
    'five': 5, 'evif': 5,
    'six': 6, 'xis': 6,
    'seven': 7, 'neves': 7,
    'eight': 8, 'thgie': 8,
    'nine': 9, 'enin': 9}

calibration_value = 0
with open(filename) as f:
    for line in f:
        first_digit = re.search(digits, line).group()
        last_digit = re.search(digits_reversed, line[::-1]).group()
        calibration_value += int(make_number(first_digit)) * 10 + int(make_number(last_digit))

print(calibration_value)
