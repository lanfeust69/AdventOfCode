import sys
sys.setrecursionlimit(1500)

strongest, strongest_r = -1, 0
robots = []
for line in open('test.in'):
    p, r = line.rstrip().split(', ')
    p, r = tuple(map(int, p[5:-1].split(','))), int(r[2:])
    if r > strongest_r:
        strongest_r = r
        strongest = len(robots)
    robots.append((p, r))

p0, r0 = robots[strongest]
nb_in_range = 0
for p, _ in robots:
    if sum(abs(p[i] - p0[i]) for i in range(3)) <= r0:
        nb_in_range += 1

print(nb_in_range)

nb = len(robots)

max_set_size = 0
max_sets = []

def find_clique(selected, pos):
    global max_set_size
    if pos == nb:
        if len(selected) < max_set_size:
            return
        if len(selected) > max_set_size:
            max_sets.clear()
            max_set_size = len(selected)
        max_sets.append(selected[:])
        print('found', len(max_sets), 'sets of size', max_set_size)
        print([(i, robots[i]) for i in range(nb) if i not in max_sets[-1]])
        return
    if nb - pos + len(selected) < max_set_size:
        return
    p, r = robots[pos]
    ok = True
    for i in selected:
        d = sum(abs(p[j] - robots[i][0][j]) for j in range(3))
        if d > r + robots[i][1]:
            ok = False
            break
    if ok:
        selected.append(pos)
        find_clique(selected, pos + 1)
        selected.pop()
    find_clique(selected, pos + 1)

# find_clique([], 0)

# seems these have relatively few others in range, while 980 remaining constitute the unique maximal clique
outliers = [26, 167, 263, 267, 284, 293, 296, 322, 357, 418, 488, 495, 529, 609, 614, 720, 724, 869, 983, 992]

# for i in range(nb):
#     p0, r0 = robots[i]
#     nb_in_range = 0
#     for p, r in robots:
#         if sum(abs(p[i] - p0[i]) for i in range(3)) <= r0 + r:
#             nb_in_range += 1
#     if i in outliers:
#         print(i, nb_in_range)
#     elif nb_in_range < 980:
#         print(i, '!!!')

mins = [0] * 3
maxs = [0] * 3
for i in range(3):
    mins[i] = min(robots[j][0][i] for j in range(nb) if j not in outliers)
    maxs[i] = max(robots[j][0][i] for j in range(nb) if j not in outliers)

progress = True
while progress:
    progress = False
    for i in range(nb):
        if i in outliers:
            continue
        c, r = robots[i]
        for j in range(3):
            min_d = 0
            for k in range(3):
                if k == j:
                    continue
                if c[k] < mins[k]:
                    min_d += mins[k] - c[k]
                if c[k] > maxs[k]:
                    min_d += c[k] - maxs[k]
            if min_d > r:
                raise ValueError('?')
            if mins[j] < c[j] - (r - min_d):
                progress = True
                mins[j] = c[j] - (r - min_d)
            if maxs[j] > c[j] + (r - min_d):
                progress = True
                maxs[j] = c[j] + (r - min_d)
    for i in range(nb):
        if i in outliers:
            continue
        c, r = robots[i]
        for j in range(3):
            if c[j] + r < mins[j]:
                raise ValueError('?')

print(mins, maxs)

def dist(a, b):
    return sum(abs(a[i] - b[i]) for i in range(3))

p = tuple(mins)

rs = [i for i in range(nb) if i not in outliers]
min_reach, min_reach_dist = -1, 0
max_reach, max_reach_dist = -1, 0
for i in rs:
    d = sum(robots[i][0])
    if min_reach == -1 or d + robots[i][1] < min_reach_dist:
        min_reach_dist = d + robots[i][1]
        min_reach = i
    if max_reach == -1 or d - robots[i][1] > max_reach_dist:
        max_reach_dist = d - robots[i][1]
        max_reach = i

print(min_reach_dist, max_reach_dist)
