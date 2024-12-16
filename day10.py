grid = [[int(c) for c in line.rstrip()] for line in open('test.in')]

h, w = len(grid), len(grid[0])

nbs = [[0] * w for _ in range(h)]
reachable = [[set() for _ in range(w)] for _ in range(h)]

res = 0
res2 = 0
for i in range(9, -1, -1):
    for r in range(h):
        for c in range(w):
            if grid[r][c] != i:
                continue
            if i == 9:
                nbs[r][c] = 1
                reachable[r][c].add((r, c))
            else:
                nb = 0
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == i + 1:
                        nb += nbs[rr][cc]
                        reachable[r][c].update(reachable[rr][cc])
                nbs[r][c] = nb
                if i == 0:
                    res += len(reachable[r][c])
                    res2 += nb

print(res)
print(res2)
