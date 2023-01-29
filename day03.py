claims = []
for line in open('test.in'):
    tokens = line.rstrip().split()
    claims.append(tuple(map(int, tokens[-2][:-1].split(','))) + tuple(map(int, tokens[-1].split('x'))))

max_w = max(t[0] + t[2] for t in claims)
max_h = max(t[1] + t[3] for t in claims)

grid = [[0] * max_w for _ in range(max_h)]
ids = [[-1] * max_w for _ in range(max_h)]
candidates = set()
for id in range(len(claims)):
    x, y, w, h = claims[id]
    overlaps = False
    for i in range(h):
        for j in range(w):
            grid[y + i][x + j] += 1
            if ids[y + i][x + j] != -1:
                overlaps = True
                if ids[y + i][x + j] in candidates:
                    candidates.remove(ids[y + i][x + j])
            else:
                ids[y + i][x + j] = id
    if not overlaps:
        candidates.add(id)

print(sum(sum(n > 1 for n in row) for row in grid))
print(candidates.pop() + 1)
