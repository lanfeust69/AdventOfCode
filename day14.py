grid = [[c for c in line.rstrip()] for line in open('test.in')]

h, w = len(grid), len(grid[0])

def set_grid(r, c, v):
    grid[r][c] = v

def roll(dir):
    if dir in 'NS':
        outer = range(w)
        inner = range(h)
        if dir == 'N':
            getter = lambda x, y: grid[y][x]
            setter = lambda x, y, v: set_grid(y, x, v)
        else:
            getter = lambda x, y: grid[h - 1 - y][x]
            setter = lambda x, y, v: set_grid(h - 1 - y, x, v)
    else:
        outer = range(h)
        inner = range(w)
        if dir == 'W':
            getter = lambda x, y: grid[x][y]
            setter = lambda x, y, v: set_grid(x, y, v)
        else:
            getter = lambda x, y: grid[x][w - 1 - y]
            setter = lambda x, y, v: set_grid(x, w - 1 - y, v)
    for x in outer:
        target = 0
        for y in inner:
            if getter(x, y) != 'O':
                if getter(x, y) == '#':
                    target = y
                continue
            while target < y and getter(x, target) != '.':
                target += 1
            if target < y:
                setter(x, target, 'O')
                setter(x, y, '.')

def signature(grid):
    return tuple(tuple(row[i] == 'O' for i in range(w)) for row in grid)
def weight(sig):
    return sum(sum(sig[r]) * (h - r) for r in range(h))

backup = [row[:] for row in grid]
roll('N')
print(weight(signature(grid)))
grid = [row[:] for row in backup]

step = 0
sig = signature(grid)
sigs = [sig]
seen = {sig: step}
while True:
    step += 1
    for dir in 'NWSE':
        roll(dir)
    sig = signature(grid)
    if sig in seen:
        start = seen[sig]
        missing = 1000000000 - step
        equivalent = start + missing % (step - start)
        print(weight(sigs[equivalent]), 'period is', step - start, 'after', start)
        break
    sigs.append(sig)
    seen[sig] = step
