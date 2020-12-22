
# start = sum(1 << i for i, c in enumerate('....##..#.#..##..#..#....') if c == '#')
start = sum(1 << i for i, c in enumerate('####..###..#..###.#####..') if c == '#')

masks = [1 << i for i in range(25)]
neighbors = [[] for i in range(25)]
for r in range(5):
    for c in range(5):
        id = r * 5 + c
        for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr, cc = r + dr, c + dc
            if rr >= 0 and rr < 5 and cc >= 0 and cc < 5:
                neighbors[id].append(rr * 5 + cc)

def step(state):
    res = 0
    for i in range(25):
        survives = (state & masks[i]) and sum(1 for j in neighbors[i] if state & masks[j]) == 1
        appears = not (state & masks[i]) and sum(1 for j in neighbors[i] if state & masks[j]) in [1, 2]
        if survives or appears:
            res += 1 << i
    return res

seen = set([start])
state = start
while True:
    state = step(state)
    if state in seen:
        print(state)
        break
    seen.add(state)

def get_neighbors(p):
    r, c, z = p
    res = []
    for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        rr, cc = r + dr, c + dc
        if rr < 0:
            res.append((1, 2, z - 1))
        elif rr > 4:
            res.append((3, 2, z - 1))
        elif cc < 0:
            res.append((2, 1, z - 1))
        elif cc > 4:
            res.append((2, 3, z - 1))
        elif rr == 2 and cc == 2:
            if r == 1:
                res += [(0, i, z + 1) for i in range(5)]
            elif r == 3:
                res += [(4, i, z + 1) for i in range(5)]
            elif c == 1:
                res += [(i, 0, z + 1) for i in range(5)]
            elif c == 3:
                res += [(i, 4, z + 1) for i in range(5)]
        else:
            res.append((rr, cc, z))
    return res

current = set([(r, c, 0) for r in range(5) for c in range(5) if '####..###..#..###.#####..'[r * 5 + c] == '#'])
for step in range(200):
    # print('step', step)
    # min_z, max_z = min(p[2] for p in current), max(p[2] for p in current)
    # for z in range(min_z, max_z + 1):
    #     print('z =', z)
    #     for r in range(5):
    #         line = ''
    #         for c in range(5):
    #             line += '#' if (r, c, z) in current else ('?' if r == 2 and c == 2 else '.')
    #         print(line)
    after = set()
    to_check_for_birth = {}
    for p in current:
        neighs = get_neighbors(p)
        nb = 0
        for neigh in neighs:
            if neigh in current:
                nb += 1
            else:
                to_check_for_birth[neigh] = to_check_for_birth.get(neigh, 0) + 1
        if nb == 1:
            after.add(p)
    for p, nb in to_check_for_birth.items():
        if nb in [1, 2]:
            after.add(p)
    current = after

print(len(current))
