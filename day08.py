h, w = 6, 50

grid = [[False] * w for _ in range(h)]

for line in open('test.in'):
    if line.startswith('rect'):
        ww, hh = map(int, line[5:].split('x'))
        for r in range(hh):
            for c in range(ww):
                grid[r][c] = True
        continue
    # rotate
    _, d, loc, _, shift = line.rstrip().split()
    loc = int(loc.split('=')[1])
    shift = int(shift)
    if d == 'row':
        grid[loc] = grid[loc][-shift:] + grid[loc][:-shift]
    else:
        new_col = [grid[(r + h - shift) % h][loc] for r in range(h)]
        for r in range(h):
            grid[r][loc] = new_col[r]

print(sum(sum(row) for row in grid))

for row in grid:
    print(''.join('#' if b else ' ' for b in row))
# -> EOARGPHYAO
