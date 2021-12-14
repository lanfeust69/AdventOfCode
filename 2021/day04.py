draw = None
grids = []
for line in open('test.in'):
    if draw is None:
        draw = list(map(int, line.split(',')))
        continue
    if line == '\n':
        cur_grid = [None] * 5
        grids.append(cur_grid)
        r = 0
        continue
    cur_grid[r] = list(map(int, line.split()))
    r += 1

state = [[[False] * 5 for _ in range(5)] for _ in range(len(grids))]
not_won = set(range(len(grids)))
for x in draw:
    to_remove = []
    for i in not_won:
        grid = grids[i]
        for r in range(5):
            for c in range(5):
                if grid[r][c] != x:
                    continue
                state[i][r][c] = True
                if all(state[i][r][j] for j in range(5)) or all(state[i][j][c] for j in range(5)):
                    if len(not_won) == 1:
                        a = 0
                        for rr in range(5):
                            for cc in range(5):
                                if not state[i][rr][cc]:
                                    a += grid[rr][cc]
                        print('grid', i, 'won :', a * x)
                        exit(0)
                    to_remove.append(i)
    for i in to_remove:
        not_won.remove(i)
