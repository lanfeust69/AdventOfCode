import heapq

# t_x, t_y = 10, 10
# depth = 510
t_x, t_y = 10, 785
depth = 5616

h, w = t_y + 1, t_x + 1
mod = 20183

grid = [[(i * 16807 + depth) % mod for i in range(w)]]
for r in range(1, h):
    row = [(r * 48271 + depth) % mod]
    for c in range(1, w):
        row.append((grid[-1][c] * row[-1] + depth) % mod)
    grid.append(row)

grid[h - 1][w - 1] = depth % mod

def get_terrain(x, y):
    if x < 0 or y < 0:
        return -1
    while x >= len(grid[0]):
        c = len(grid[0])
        for r in range(len(grid)):
            if r == 0:
                grid[r].append((c * 16807 + depth) % mod)
            else:
                grid[r].append((grid[r][-1] * grid[r - 1][c] + depth) % mod)
    while y >= len(grid):
        row = [(len(grid) * 48271 + depth) % mod]
        for c in range(1, len(grid[0])):
            row.append((grid[-1][c] * row[-1] + depth) % mod)
        grid.append(row)
    return grid[y][x] % 3

print(sum(get_terrain(x, y) for x in range(t_x + 1) for y in range(t_y + 1)))

# equipment : 0 -> none, 1 -> torch, 2 -> climb, so that terrain t cannot use equipment t

def neighbors(x, y, e):
    t = get_terrain(x, y)
    if t == 0:
        yield (x, y, (2 if e == 1 else 1)), 7
    elif t == 1:
        yield (x, y, (2 if e == 0 else 0)), 7
    else:
        yield (x, y, (1 if e == 0 else 0)), 7
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        xx, yy = x + dx, y + dy
        tt = get_terrain(xx, yy)
        if tt != -1 and e != tt:
            yield (xx, yy, e), 1


dists = {(0, 0, 1): 0}
todo = [(0, (0, 0, 1))]
while len(todo) > 0:
    dist, state = heapq.heappop(todo)
    if state == (t_x, t_y, 1):
        print(dist)
        break
    if dists[state] < dist:
        continue
    for neigh, cost in neighbors(*state):
        if neigh in dists and dists[neigh] <= dist + cost:
            continue
        dists[neigh] = dist + cost
        heapq.heappush(todo, (dist + cost, neigh))
