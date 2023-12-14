grid = [line.rstrip() for line in open('test.in')]
h, w = len(grid), len(grid[0])

neighs_map = {
    '.': [],
    'S': [(-1, 0), (1, 0), (0, -1), (0, 1)],
    '-': [(0, -1), (0, 1)],
    '|': [(-1, 0), (1, 0)],
    'F': [(1, 0), (0, 1)],
    '7': [(1, 0), (0, -1)],
    'J': [(-1, 0), (0, -1)],
    'L': [(-1, 0), (0, 1)]
}
neigh_comp = {(-1, 0): 'S|F7', (1, 0): 'S|LJ', (0, -1): 'S-LF', (0, 1): 'S-J7'}
def neighbors(p):
    r, c = p
    for dr, dc in neighs_map[grid[r][c]]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] in neigh_comp[(dr, dc)]:
            yield rr, cc

start = -1, -1
for r in range(len(grid)):
    if 'S' in grid[r]:
        start = r, grid[r].index('S')
        break

dists = [[-1] * w for _ in range(h)]
dists[start[0]][start[1]] = 0
todo = [(start, 0)]
res = 0
end = -1, -1
while len(todo):
    next_todo = []
    for p, d in todo:
        for neigh in neighbors(p):
            if dists[neigh[0]][neigh[1]] != -1:
                continue
            dists[neigh[0]][neigh[1]] = d + 1
            if d + 1 > res:
                res = d + 1
                end = neigh
            next_todo.append((neigh, d + 1))
    todo = next_todo

print(res)

zone = [[-1] * w for _ in range(h)]
zone[end[0]][end[1]] = 0
border = {}
begin = -1, -1
for neigh in neighbors(end):
    if begin == (-1, -1):
        begin = neigh
        border[begin] = end
        zone[begin[0]][begin[1]] = 0
    else:
        border[end] = neigh
        end = neigh
        zone[end[0]][end[1]] = 0
while begin != start:
    for neigh in neighbors(begin):
        if neigh not in border:
            border[neigh] = begin
            begin = neigh
            zone[begin[0]][begin[1]] = 0
            break
    for neigh in neighbors(end):
        if neigh not in border:
            border[end] = neigh
            end = neigh
            zone[end[0]][end[1]] = 0
            break
border[end] = start

zone_size = [0] * 3

def flood_fill(point, z):
    todo = [point]
    zone[point[0]][point[1]] = z
    zone_size[z] += 1
    while len(todo):
        next_todo = []
        for p in todo:
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r, c = p[0] + dr, p[1] + dc
                if 0 <= r < h and 0 <= c < w and zone[r][c] == -1:
                    zone[r][c] = z
                    zone_size[z] += 1
                    next_todo.append((r, c))
        todo = next_todo

clock_wise = {
    (-1, 0): [(0, -1), (-1, 0), (0, 1)],
    (1, 0): [(0, 1), (1, 0), (0, -1)],
    (0, -1): [(1, 0), (0, -1), (-1, 0)],
    (0, 1): [(-1, 0), (0, 1), (1, 0)]
}

prev = start
cur = border[start]

while True:
    z = 1
    next_cur = border[cur]
    for dr, dc in clock_wise[(cur[0] - prev[0], cur[1] - prev[1])]:
        r, c = cur[0] + dr, cur[1] + dc
        if r < 0 or r >= h or c < 0 or c >= w:
            continue
        if (r, c) == next_cur:
            z = 2
        elif zone[r][c] == -1:
            flood_fill((r, c), z)
        elif zone[r][c] != z and zone[r][c] != 0:
            raise ValueError('inconsistent zoning !')
    prev, cur = cur, next_cur
    if prev == start:
        break

print(min(zone_size[1], zone_size[2]))
