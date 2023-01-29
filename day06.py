points = [tuple(map(int, line.rstrip().split(', '))) for line in open('test.in')]
nb = len(points)

seen = set(points)
borders = [set([p]) for p in points]
sizes = [1] * nb

finished = {}
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(1000):
    new_borders = [set() for _ in range(nb)]
    same_dists = set()
    ids = {}
    for i in range(nb):
        for p in borders[i]:
            for dx, dy in dirs:
                pp = p[0] + dx, p[1] + dy
                if pp in seen:
                    continue
                if pp in ids and ids[pp] != i:
                    new_borders[ids[pp]].discard(pp)
                    same_dists.add(pp)
                else:
                    ids[pp] = i
                    new_borders[i].add(pp)
    seen.update(same_dists)
    for i in range(nb):
        if len(new_borders[i]) == 0:
            finished[i] = sizes[i]
        else:
            sizes[i] += len(new_borders[i])
            seen.update(new_borders[i])
    borders = new_borders

print(max(finished.values()))

nb_safe = 0
for x in range(400):
    for y in range(400):
        s = 0
        for xx, yy in points:
            s += abs(xx - x) + abs(yy - y)
            if s >= 10000:
                break
        if s < 10000:
            nb_safe += 1

print(nb_safe)
