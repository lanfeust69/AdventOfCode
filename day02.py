d1 = 4
d2 = 10
code1 = ''
code2 = ''
keypad = [['', '', '1', '', ''], ['', '2', '3', '4', ''], ['5', '6', '7', '8', '9'], ['', 'A', 'B', 'C', ''], ['', '', 'D', '', '']]

for line in open('test.in'):
    for c in line.rstrip():
        if c == 'L':
            if d1 % 3 > 0:
                d1 -= 1
            if d2 % 5 > 0 and keypad[d2 // 5][d2 % 5 - 1]:
                d2 -= 1
        if c == 'R':
            if d1 % 3 < 2:
                d1 += 1
            if d2 % 5 < 4 and keypad[d2 // 5][d2 % 5 + 1]:
                d2 += 1
        if c == 'U':
            if d1 > 2:
                d1 -= 3
            if d2 > 4 and keypad[d2 // 5 - 1][d2 % 5]:
                d2 -= 5
        if c == 'D':
            if d1 < 6:
                d1 += 3
            if d2 < 20 and keypad[d2 // 5 + 1][d2 % 5]:
                d2 += 5
    code1 += str(d1 + 1)
    code2 += keypad[d2 // 5][d2 % 5]

print(code1)
print(code2)
