forest = []
for line in open('test.in'):
    forest.append(line.rstrip())

h, w = len(forest), len(forest[0])
seen = set()
for r in range(h):
    cur_left, cur_right = -1, -1
    for c in range(w):
        hh = int(forest[r][c])
        if hh > cur_left:
            seen.add((r, c))
            cur_left = hh
        hh = int(forest[r][w - 1 - c])
        if hh > cur_right:
            seen.add((r, w - 1 - c))
            cur_right = hh
for c in range(w):
    cur_top, cur_bottom = -1, -1
    for r in range(h):
        hh = int(forest[r][c])
        if hh > cur_top:
            seen.add((r, c))
            cur_top = hh
        hh = int(forest[h - 1 - r][c])
        if hh > cur_bottom:
            seen.add((h - 1 - r, c))
            cur_bottom = hh

print(len(seen))

best = 0
for r in range(1, h - 1):
    for c in range(1, w - 1):
        hh = int(forest[r][c])
        v = 1
        for d in range(1, r + 1):
            if int(forest[r - d][c]) >= hh:
                break
        v *= d
        for d in range(1, h - r):
            if int(forest[r + d][c]) >= hh:
                break
        v *= d
        for d in range(1, c + 1):
            if int(forest[r][c - d]) >= hh:
                break
        v *= d
        for d in range(1, w - c):
            if int(forest[r][c + d]) >= hh:
                break
        v *= d
        best = max(best, v)

print(best)
