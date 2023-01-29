grid = [line.rstrip() for line in open('test.in')]

puzzle = set()
n = len(grid)
for r in range(n):
    for c in range(n):
        if grid[r][c] == '#':
            puzzle.add((c - n // 2, n // 2 - r))

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

infected = set(puzzle)
x, y, d = 0, 0, 0
res = 0
for burst in range(10000):
    if (x, y) in infected:
        d = (d + 1) % 4
        infected.remove((x, y))
    else:
        d = (d + 3) % 4
        infected.add((x, y))
        res += 1
    x, y = x + dirs[d][0], y + dirs[d][1]
    if burst in [6, 69]:
        print(res)

print(res)

infected = set(puzzle)
weakened = set()
flagged = set()
x, y, d = 0, 0, 0
res = 0
for burst in range(10000000):
    if (x, y) in infected:
        d = (d + 1) % 4
        infected.remove((x, y))
        flagged.add((x, y))
    elif (x, y) in weakened:
        weakened.remove((x, y))
        res += 1
        infected.add((x, y))
    elif (x, y) in flagged:
        d = (d + 2) % 4
        flagged.remove((x, y))
    else:
        d = (d + 3) % 4
        weakened.add((x, y))
    x, y = x + dirs[d][0], y + dirs[d][1]
    if burst  == 99:
        print(res)

print(res)
