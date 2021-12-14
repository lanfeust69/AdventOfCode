aim, x, depth = 0, 0, 0
for line in open('test.in'):
    p = line.split()
    d = int(p[1])
    if p[0] == 'forward':
        x += d
        depth += d * aim
    elif p[0] == 'up':
        aim -= d
    else:
        aim += d

print(x * depth)
