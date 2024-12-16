grid = [line.rstrip() for line in open('test.in')]

h, w = len(grid), len(grid[0])

xmas = 'XMAS'

total = 0
for r in range(h):
    for c in range(w):
        if grid[r][c] == 'X':
            nb = 0
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    ok = True
                    if (dr, dc) == (0, 0):
                        continue
                    for i in range(4):
                        rr, cc = r + dr * i, c + dc * i
                        if not (0 <= rr < h and 0 <= cc < w and grid[rr][cc] == xmas[i]):
                            ok = False
                            break
                    if ok:
                        total += 1

print(total)

nbs = [[0] * w for _ in range(h)]
total = 0
for i in range(3, -1, -1):
    for r in range(h):
        for c in range(w):
            if grid[r][c] == xmas[i]:
                if i == 3:
                    nbs[r][c] = 1
                else:
                    nb = 0
                    for dr in range(-1, 2):
                        for dc in range(-1, 2):
                            rr, cc = r + dr, c + dc
                            if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == xmas[i + 1]:
                                nb += nbs[rr][cc]
                    nbs[r][c] = nb
                    if i == 0:
                        total += nb

print(total)

total = 0
for r in range(1, h - 1):
    for c in range(1, w - 1):
        if grid[r][c] != 'A':
            continue
        if grid[r - 1][c - 1] + grid[r + 1][c + 1] in ('MS', 'SM') and grid[r - 1][c + 1] + grid[r + 1][c - 1] in ('MS', 'SM'):
            total += 1

print(total)
