import re

filename = '1.1input.txt'
# filename = '1.1test.txt'

calibration_value = 0
with open(filename) as f:
    for line in f:
        first_digit = re.search('[0-9]', line).group()
        last_digit = re.search('[0-9]', line[::-1]).group()
        calibration_value += int(first_digit) * 10 + int(last_digit)

print(calibration_value)
