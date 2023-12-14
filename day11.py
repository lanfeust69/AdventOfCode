grid = [line.rstrip() for line in open('test.in')]
h, w = len(grid), len(grid[0])
mult = 1000000

empty_rows = []
for r in range(h):
    if '#' not in grid[r]:
        empty_rows.append(r)
empty_cols = []
for c in range(w):
    if all(grid[r][c] == '.' for r in range(h)):
        empty_cols.append(c)
rows_dist = [[-1] * h for _ in range(h)]
cols_dist = [[-1] * w for _ in range(w)]
def delta(a, b, is_row):
    if a > b:
        return delta(b, a, is_row)
    cache = rows_dist if is_row else cols_dist
    if cache[a][b] != -1:
        return cache[a][b]
    res = b - a
    empty = empty_rows if is_row else empty_cols
    for e in empty:
        if e < a:
            continue
        if e > b:
            break
        res += mult - 1
    cache[a][b] = res
    return res

galaxies = []
for r in range(h):
    for c in range(w):
        if grid[r][c] == '#':
            galaxies.append((r, c))

res = 0
dists = {}
for i in range(len(galaxies) - 1):
    ri, ci = galaxies[i]
    for j in range(i + 1, len(galaxies)):
        rj, cj = galaxies[j]
        d = delta(ri, rj, True) + delta(ci, cj, False)
        dists[(i, j)] = d
        res += d

print(res)
