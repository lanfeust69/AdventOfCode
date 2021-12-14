folds = []
dots = []
for line in open('test.in'):
    if line.startswith('fold'):
        d, v = line[11:].split('=')
        folds.append((d, int(v)))
    elif len(line) > 1:
        dots.append(tuple(map(int, line.split(','))))

h = 2 * max(t[1] for t in folds if t[0] == 'y') + 1
w = 2 * max(t[1] for t in folds if t[0] == 'x') + 1
grid = [[False] * w for _ in range(h)]
for c, r in dots:
    grid[r][c] = True

def fold(f):
    d, v = f
    if d == 'y':
        return [[grid[r][c] or grid[v * 2 - r][c] for c in range(w)] for r in range(v)]
    else:
        return [[grid[r][v - 1 - c] or grid[r][v + 1 + c] for c in range(v)] for r in range(h)]

# grid = fold(folds[0])
# print(sum(sum(l) for l in grid))

for f in folds:
    grid = fold(f)
    h = len(grid)
    w = len(grid[0])

for l in grid:
    print(''.join('#' if i else ' ' for i in reversed(l)))
