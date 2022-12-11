grid = []
def add_point(x, y):
    if x >= 1000:
        raise ValueError('bigger than expected')
    while y >= len(grid):
        grid.append([False] * 1000)
    grid[y][x] = True

for line in open('test.in'):
    points = [tuple(map(int, p.split(','))) for p in line.rstrip().split(' -> ')]
    x0, y0 = points[0]
    add_point(x0, y0)
    for i in range(1, len(points)):
        x1, y1 = points[i]
        dx = 0 if x0 == x1 else (x1 - x0) // abs(x1 - x0)
        dy = 0 if y0 == y1 else (y1 - y0) // abs(y1 - y0)
        while x0 != x1 or y0 != y1:
            x0, y0 = x0 + dx, y0 + dy
            add_point(x0, y0)

grid.append([False] * 1000)
grid.append([True] * 1000)

nb = 0
done = False
while not done:
    x, y = 500, 0
    while True:
        if y == len(grid) - 1:
            done = True
            break
        if not grid[y + 1][x]:
            y = y + 1
            continue
        if not grid[y + 1][x - 1]:
            x, y = x - 1, y + 1
            continue
        if not grid[y + 1][x + 1]:
            x, y = x + 1, y + 1
            continue
        add_point(x, y)
        nb += 1
        break
    if (x, y) == (500, 0):
        done = True

print(nb)
