grid = [[int(c) for c in line[:-1]] for line in open('test.in')]
h = len(grid)
w = len(grid[0])
def neighbors(r, c):
    if r > 0:
        yield (r - 1, c)
    if r < h - 1:
        yield (r + 1, c)
    if c > 0:
        yield (r, c - 1)
    if c < w - 1:
        yield (r, c + 1)

lows = [(r, c) for r in range(h) for c in range(w) if all(grid[rr][cc] > grid[r][c] for rr, cc in neighbors(r, c))]
sizes = []
for r0, c0 in lows:
    basin = set([(r0, c0)])
    todo = [(r0, c0)]
    while len(todo) > 0:
        next_todo = []
        for r, c in todo:
            for rr, cc in neighbors(r, c):
                if (rr, cc) in basin or grid[rr][cc] == 9:
                    continue
                level = set([(rr, cc)])
                height = grid[rr][cc]
                todo2 = [(rr, cc)]
                while len(todo2) > 0:
                    next_todo2 = []
                    for (rrr, ccc) in todo2:
                        for n in neighbors(rrr, ccc):
                            if n in level or grid[n[0]][n[1]] != height:
                                continue
                            level.add(n)
                            next_todo2.append(n)
                    todo2 = next_todo2
                if all(p in basin or p in level or grid[p[0]][p[1]] > height for p in neighbors(rrr, ccc) for rrr, ccc in level):
                    basin.update(level)
                    next_todo += list(level)
        todo = next_todo
    sizes.append(len(basin))

sizes.sort()
print(sizes[-10:])
print(sizes[-1] * sizes[-2] * sizes[-3])
