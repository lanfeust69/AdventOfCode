grid = [[False] * 1000 for _ in range(1000)]
bad = set()
for line in open('test.in'):
    (x0, y0), (x1, y1) = map(lambda s: tuple(map(int, s.split(','))), line.split(' -> '))
    dx, dy = 0, 0
    if x0 < x1:
        dx = 1
    elif x0 > x1:
        dx = -1
    if y0 < y1:
        dy = 1
    elif y0 > y1:
        dy = -1
    x, y = x0, y0
    while True:
        if grid[x][y]:
            bad.add((x, y))
        else:
            grid[x][y] = True
        if (x, y) == (x1, y1):
            break
        x, y = x + dx, y + dy

print(len(bad))
