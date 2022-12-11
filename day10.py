cycle = 0
x = 1
screen = [['.'] * 40 for _ in range(6)]
s = 0
for line in open('test.in'):
    line = line.rstrip()
    if x - 1 <= cycle % 40 <= x + 1:
        screen[cycle // 40 % 6][cycle % 40] = '#'
    if cycle % 40 == 20:
        s += x * cycle
    cycle += 1
    if line == 'noop':
        continue
    if x - 1 <= cycle % 40 <= x + 1:
        screen[cycle // 40 % 6][cycle % 40] = '#'
    if cycle % 40 == 20:
        s += x * cycle
    x += int(line.split()[1])
    cycle += 1

print(s)
for row in screen:
    print(''.join(row))
