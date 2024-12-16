grid = [line.rstrip() for line in open('test.in')]

h, w = len(grid), len(grid[0])

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
border_pos = [(0, 1), (0, 0), (1, 0), (0, 0)]

res1 = 0
res2 = 0
visited = [[False] * w for _ in range(h)]
for r in range(h):
    for c in range(w):
        if visited[r][c]:
            continue
        visited[r][c] = True
        perimeter = 0
        border = []
        area = 1
        todo = [(r, c)]
        while len(todo):
            new_todo = []
            for (rr, cc) in todo:
                for d in range(4):
                    dr, dc = dirs[d]
                    rrr, ccc = rr + dr, cc + dc
                    if 0 <= rrr < h and 0 <= ccc < w and grid[rrr][ccc] == grid[r][c]:
                        if not visited[rrr][ccc]:
                            visited[rrr][ccc] = True
                            area += 1
                            new_todo.append((rrr, ccc))
                    else:
                        perimeter += 1
                        (rs, cs) = border_pos[d]
                        border.append((rr + rs, cc + cs, d))
            todo = new_todo
        res1 += perimeter * area
        nb = 0
        for d in range(4):
            by_line = {}
            for segment in border:
                if segment[2] == d:
                    coord = 1 - d // 2
                    if segment[coord] in by_line:
                        by_line[segment[coord]].append(segment[1 - coord])
                    else:
                        by_line[segment[coord]] = [segment[1 - coord]]
            for _, v in by_line.items():
                v.sort()
                prev = -10
                for p in v:
                    if p != prev + 1:
                        nb += 1
                    prev = p
        res2 += area * nb

print(res1)
print(res2)
