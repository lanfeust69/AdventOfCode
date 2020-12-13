file = open('test.in')
grid = [line[:-1] for line in file.readlines()]

asteroids = set()
for y, l in enumerate(grid):
    for x, c in enumerate(l):
        if c == '#':
            asteroids.add((x, y))

def gcd(a, b): return a if b == 0 else gcd(b, a % b)

best_val = 0
best = None
best_in_sight = {}
for asteroid in asteroids:
    in_sight = {}
    for other in asteroids:
        if other == asteroid:
            continue
        dx, dy = other[0] - asteroid[0], other[1] - asteroid[1]
        g = gcd(abs(dx), abs(dy))
        dx, dy = dx // g, dy // g
        if (dx, dy) in in_sight:
            in_sight[(dx, dy)].add(g)
        else:
            in_sight[(dx, dy)] = set([g])
    if len(in_sight) > best_val:
        best_val = len(in_sight)
        best = asteroid
        best_in_sight = in_sight

print(best, best_val)

targets = best_in_sight
first_quadrant = sorted((dir for dir in targets if dir[0] >= 0 and dir[1] < 0), key=lambda dir: -dir[0] / dir[1])
second_quadrant = sorted((dir for dir in targets if dir[0] >= 0 and dir[1] > 0), key=lambda dir: -dir[0] / dir[1])
third_quadrant = sorted((dir for dir in targets if dir[0] < 0 and dir[1] > 0), key=lambda dir: -dir[0] / dir[1])
fourth_quadrant = sorted((dir for dir in targets if dir[0] < 0 and dir[1] < 0), key=lambda dir: -dir[0] / dir[1])
sorted_dirs = first_quadrant
if (1, 0) in targets:
    sorted_dirs.append((1, 0))
sorted_dirs += second_quadrant
sorted_dirs += third_quadrant
if (-1, 0) in targets:
    sorted_dirs.append((-1, 0))
sorted_dirs += fourth_quadrant

cur_dir = 0
for _ in range(199):
    targets[sorted_dirs[cur_dir]].remove(min(targets[sorted_dirs[cur_dir]]))
    cur_dir = (cur_dir + 1) % len(sorted_dirs)
    while len(targets[sorted_dirs[cur_dir]]) == 0:
        cur_dir = (cur_dir + 1) % len(sorted_dirs)

dir = sorted_dirs[cur_dir]
d = min(targets[dir])
res = best[0] + dir[0] * d, best[1] + dir[1] * d
print(res, res[0] * 100 + res[1])
