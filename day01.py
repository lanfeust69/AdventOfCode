for line in open('test.in'):
    insts = line.rstrip().split(', ')

x, y, d = 0, 0, 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
seen = set([(0, 0)])
found = False
for inst in insts:
    d = (d + (1 if inst[0] == 'R' else 3)) % 4
    n = int(inst[1:])
    for _ in range(n):
        x += dirs[d][0]
        y += dirs[d][1]
        if not found and (x, y) in seen:
            print(abs(x) + abs(y))
            found = True
        seen.add((x, y))

print(abs(x) + abs(y))
