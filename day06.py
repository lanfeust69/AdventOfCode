grid = [[c for c in line.rstrip()] for line in open('test.in')]
h, w = len(grid), len(grid[0])

r0, c0 = -1, -1
for r in range(h):
    for c in range(w):
        if grid[r][c] not in '#.':
            r0, c0 = r, c
            break
    if r0 != -1:
        break

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d0 = '^>v<'.index(grid[r0][c0])

visited = [[False] * w for _ in range(h)]
r, c, d = r0, c0, d0
res = 0
while True:
    if not visited[r][c]:
        visited[r][c] = True
        res += 1
    rr, cc = r + dirs[d][0], c + dirs[d][1]
    if not (0 <= rr < h and 0 <= cc < w):
        break
    if grid[rr][cc] == '#':
        d = (d + 1) % 4
    else:
        r, c = rr, cc

print(res)

res = 0
for ro in range(h):
    for co in range(w):
        if not visited[ro][co] or (ro, co) == (r0, c0):
            continue
        grid[ro][co] = '#'
        is_loop = False
        v = [[0] * w for _ in range(h)]
        r, c, d = r0, c0, d0
        while True:
            if v[r][c] & (1 << d):
                is_loop = True
                break
            else:
                v[r][c] |= 1 << d
            rr, cc = r + dirs[d][0], c + dirs[d][1]
            if not (0 <= rr < h and 0 <= cc < w):
                break
            if grid[rr][cc] == '#':
                d = (d + 1) % 4
            else:
                r, c = rr, cc
        if is_loop:
            res += 1
        grid[ro][co] = '.'

print(res)
