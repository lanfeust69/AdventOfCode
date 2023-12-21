moves = []
moves2 = []
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_names = 'RDLU'
for line in open('test.in'):
    dir, dist, color = line.rstrip().split()
    moves.append((dir_names.index(dir), int(dist), color))
    moves2.append((int(color[-2]), int(color[2:-2], 16)))

border = {}
r, c = 0, 0
for dir, dist, color in moves:
    for _ in range(dist):
        r, c = r + dirs[dir][0], c + dirs[dir][1]
        if (r, c) in border:
            print('warning : crossing at', r, c)
        border[(r, c)] = color

min_r, max_r, min_c, max_c = 1e9, -1e9, 1e9, -1e9
for r, c in border:
    min_r, max_r, min_c, max_c = min(min_r, r), max(max_r, r), min(min_c, c), max(max_c, c)

h, w = max_r - min_r + 3, max_c - min_c + 3
grid = [[0] * w for _ in range(h)]
grid[0][0] = 1
todo = [(0, 0)]
nb_outside = 1
while len(todo):
    next_todo = []
    for r, c in todo:
        for dr, dc in dirs:
            rr, cc = r + dr, c + dc
            if not (0 <= rr < h and 0 <= cc < w):
                continue
            if grid[rr][cc]:
                continue
            if (min_r + rr - 1, min_c + cc - 1) in border:
                grid[rr][cc] = 2
                continue
            grid[rr][cc] = 1
            nb_outside += 1
            next_todo.append((rr, cc))
    todo = next_todo

print(h * w - nb_outside)

r, c = 0, 0
min_r, max_r, min_c, max_c = 1e9, -1e9, 1e9, -1e9
h_lines = {}
v_lines = {}
for i in range(len(moves2)):
    dir, dist = moves2[i]
    rr, cc = r + dirs[dir][0] * dist, c + dirs[dir][1] * dist
    if dir % 2 == 0:
        seg = min(c, cc), max(c, cc)
        if r in h_lines:
            h_lines[r].append(seg)
        else:
            h_lines[r] = [seg]
    else:
        seg = min(r, rr), max(r, rr)
        if c in v_lines:
            v_lines[c].append(seg)
        else:
            v_lines[c] = [seg]
    r, c = rr, cc
    print(f'({c}, {-r})')
    min_r, max_r, min_c, max_c = min(min_r, r), max(max_r, r), min(min_c, c), max(max_c, c)

for r in h_lines:
    h_lines[r].sort()
for c in v_lines:
    v_lines[c].sort()

print(min_r, max_r, min_c, max_c)

rs = sorted(r for r in h_lines)
cs = sorted(c for c in v_lines)

print(rs, cs)

res = 0
in_segs = h_lines[rs[0]]
prev_r = rs[0]
for r in rs[1:]:
    new_in_segs = []
    points = []
    for s, e in in_segs:
        res += (r - prev_r) * (e - s + 1)
        points.append((s, 0, 0))
        points.append((e, 0, 1))
    segs = h_lines[r]
    for s, e in segs:
        points.append((s, 1, 0))
        points.append((e, 1, 1))
    points.sort()
    inside = False
    in_remove = False
    skip = False
    for i in range(len(points)):
        if skip:
            skip = False
            continue
        if i < len(points) - 1 and points[i][0] == points[i + 1][0]:
            skip = True
            if not inside:
                if in_remove:
                    res += points[i][0] - remove_start + 1
                    in_remove = False
                else:
                    remove_start = points[i][0]
                    in_remove = True
            continue
        inside = not inside
        if inside:
            start = points[i][0]
            if in_remove:
                res += points[i][0] - remove_start
                in_remove = False
        else:
            new_in_segs.append((start, points[i][0]))
            if points[i][1] == 1 and points[i][2] == 0:
                remove_start = points[i][0] + 1
                in_remove = True
    in_segs = new_in_segs
    prev_r = r

print(res)
