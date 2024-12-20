corrupted = [tuple(map(int, line.rstrip().split(','))) for line in open('test.in')]
h, w = 71, 71

grid = [[True] * w for _ in range(h)]
for x, y in corrupted[:1024]:
    grid[x][y] = False

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def solve():
    visited = [[False] * w for _ in range(h)]
    todo = [(0, 0)]
    visited[0][0] = True
    dist = 0
    while len(todo):
        dist += 1
        next_todo = []
        for (r, c) in todo:
            for (dr, dc) in dirs:
                rr, cc = r + dr, c + dc
                if (rr, cc) == (h - 1, w - 1):
                    return dist
                if 0 <= rr < h and 0 <= cc < w and not visited[rr][cc] and grid[rr][cc]:
                    visited[rr][cc] = True
                    next_todo.append((rr, cc))
        todo = next_todo
    return None

print(solve())

inf, sup = 0, len(corrupted)
while inf + 1 < sup:
    mid = (inf + sup) // 2
    grid = [[True] * w for _ in range(h)]
    for x, y in corrupted[:mid]:
        grid[x][y] = False
    if solve():
        inf = mid
    else:
        sup = mid

# KO if taking "sup" bytes, failing one is the last, sup - 1 = inf
print(f'{corrupted[inf][0]},{corrupted[inf][1]}')
