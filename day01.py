s = 0
digits_strings = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}
part1 = False
for line in open('test.in'):
    line = line.rstrip()
    if part1:
        digits = [int(c) for c in line if c.isdigit()]
    else:
        digits = []
        for i in range(len(line)):
            if line[i].isdigit():
                digits.append(int(line[i]))
                break
            for ds in digits_strings:
                if line[i:i + len(ds)] == ds:
                    digits.append(digits_strings[ds])
                    break
            if len(digits):
                break
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                digits.append(int(line[i]))
                break
            for ds in digits_strings:
                if line[i:i + len(ds)] == ds:
                    digits.append(digits_strings[ds])
                    break
            if len(digits) == 2:
                break
    s += digits[0] * 10 + digits[-1]

print(s)
