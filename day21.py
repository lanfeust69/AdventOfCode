grid = [line.rstrip() for line in open('test.in')]
h, w = len(grid), len(grid[0])
r0, c0 = -1, -1
for r in range(h):
    if 'S' in grid[r]:
        r0, c0 = r, grid[r].index('S')
        break

reachable = set([(r0, c0)])
for step in range(64):
    new_reachable = set()
    for r, c in reachable:
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            rr, cc = r + dr, c + dc
            if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] != '#':
                new_reachable.add((rr, cc))
    reachable = new_reachable

print(len(reachable))

starts = [(r, c) for r in (0, h // 2, h - 1) for c in (0, w // 2, w - 1)]
dists = [[[-1] * 9 for _ in range(w)] for _ in range(h)]
for i in range(9):
    r0, c0 = starts[i]
    dists[r0][c0][i] = 0
    todo = [starts[i]]
    d = 0
    while len(todo):
        d += 1
        next_todo = []
        for r, c in todo:
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                rr, cc = r + dr, c + dc
                if rr < 0 or rr >= h or cc < 0 or cc >= w or grid[rr][cc] == '#':
                    continue
                if dists[rr][cc][i] == -1:
                    dists[rr][cc][i] = d
                    next_todo.append((rr, cc))
        todo = next_todo

# for each cell, in how many tiles is it reachable ?
max_d = 26501365
res = 0
for r in range(h):
    for c in range(w):
        if dists[r][c][4] == -1:
            continue
        total = 0
        # 0, 0
        if (r + c) % 2 == max_d % 2 and dists[r][c][4] <= max_d:
            total += 1
        # aligned
        for i in (1, 3, 5, 7):
            d0 = h // 2 + 1
            d = max_d - d0 - dists[r][c][i]
            if d < 0:
                continue
            nb = d // h + 1
            total += nb // 2
            if nb % 2 != 0 and d % 2 == 0:
                total += 1
        # others
        for i in (0, 2, 6, 8):
            d0 = h + 1
            d = max_d - d0 - dists[r][c][i]
            if d < 0:
                continue
            nb = d // h + 1
            if d % 2 == 0:
                # 1 + 3 + 5 + ... + (nb or nb - 1)
                nb = ((nb + 1) // 2)**2
            else:
                # 2 + 4 + 6 + ... + (nb or nb - 1)
                nb = (nb // 2) * (nb // 2 + 1)
            total += nb
        res += total

print(res)
