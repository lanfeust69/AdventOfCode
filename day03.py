import re

memory = ''
for line in open('test.in'):
    memory += line.rstrip()

res = 0
for m in re.finditer(r'mul\((\d+),(\d+)\)', memory):
    op1, op2 = map(int, m.group(1, 2))
    res += op1 * op2

print(res)

res = 0
enabled = True
for e in re.split(r'(do(?:n\'t)?\(\))', memory):
    if e == 'do()':
        enabled = True
    elif e == 'don\'t()':
        enabled = False
    elif enabled:
        for m in re.finditer(r'mul\((\d+),(\d+)\)', e):
            op1, op2 = map(int, m.group(1, 2))
            res += op1 * op2

print(res)
