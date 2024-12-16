import heapq

grid = [[c for c in line.rstrip()] for line in open('test.in')]
h, w = len(grid), len(grid[0])

rs, cs, re, ce = -1, -1, -1, -1
for r in range(h):
    for c in range(w):
        if grid[r][c] == 'S':
            rs, cs = r, c
            grid[r][c] = '.'
        elif grid[r][c] == 'E':
            re, ce = r, c
            grid[r][c] = '.'

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dists = [[[1000000000] * 4 for _ in range(w)] for _ in range(h)]
parents = [[[[] for _ in range(4)] for _ in range(w)] for _ in range(h)]
dists[rs][cs][0] = 0
todo = []
res = -1
heapq.heappush(todo, (0, rs, cs, 0))
while len(todo):
    dist, r, c, d = heapq.heappop(todo)
    if dist > dists[r][c][d]:
        continue
    if (r, c) == (re, ce):
        res = dist
        break
    rr, cc = r + dirs[d][0], c + dirs[d][1]
    if grid[rr][cc] == '.' and dist + 1 <= dists[rr][cc][d]:
        if dist + 1 < dists[rr][cc][d]:
            dists[rr][cc][d] = dist + 1
            heapq.heappush(todo, (dist + 1, rr, cc, d))
            parents[rr][cc][d].clear()
        parents[rr][cc][d].append((r, c, d))
    for i in (1, 3):
        dd = (d + i) % 4
        if dist + 1000 <= dists[r][c][dd]:
            if dist + 1000 < dists[r][c][dd]:
                dists[r][c][dd] = dist + 1000
                heapq.heappush(todo, (dist + 1000, r, c, dd))
                parents[r][c][dd].clear()
            parents[r][c][dd].append((r, c, d))

print(res)

on_path = [[False] * w for _ in range(h)]
on_path[re][ce] = True
todo = [(re, ce, i) for i in range(4) if dists[re][ce][i] == res]
while len(todo):
    next_todo = []
    for (r, c, d) in todo:
        for (rr, cc, dd) in parents[r][c][d]:
            on_path[rr][cc] = True
            next_todo.append((rr, cc, dd))
    todo = next_todo

print(sum(sum(row) for row in on_path))
