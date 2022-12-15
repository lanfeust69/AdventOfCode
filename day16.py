raw_input = [line.rstrip().split() for line in open('test.in')]
nb_valves = len(raw_input)
ids = {}
for i in range(nb_valves):
    ids[raw_input[i][1]] = i

flows = [0] * nb_valves
with_flow = []
graph = [[] for _ in range(nb_valves)]
for i in range(nb_valves):
    flows[i] = int(raw_input[i][4][5:-1])
    if flows[i] > 0:
        with_flow.append(i)
    for neigh in raw_input[i][9:]:
        graph[i].append(ids[neigh[:2]])

nb_useful = len(with_flow)
all_useful = (1 << nb_useful) - 1

cache = [[[(-1, False, -1)] * (1 << nb_useful) for _ in range(30)] for _ in range(nb_valves)]

def solve(valve, time, used):
    if time >= 29 or used == all_useful:
        return 0
    if cache[valve][time][used][0] != -1:
        return cache[valve][time][used][0]
    best, best_neigh, best_is_with = 0, -1, False
    if_open, idx = 0, 0
    if valve in with_flow:
        idx = with_flow.index(valve)
        if used & (1 << idx) == 0:
            if_open = flows[valve] * (30 - time - 1)
    for neigh in graph[valve]:
        sub = solve(neigh, time + 1, used)
        if sub > best:
            best, best_is_with, best_neigh = sub, False, neigh
        if if_open > 0:
            sub = if_open + solve(neigh, time + 2, used | (1 << idx))
            if sub > best:
                best, best_is_with, best_neigh = sub, True, neigh

    cache[valve][time][used] = best, best_is_with, best_neigh
    return best

res = solve(ids['AA'], 0, 0)
print(res)

cache2 = {}
nb_strange = 0

def solve2(valve1, valve2, time, used):
    if time >= 25:
        return 0
    if used == all_useful:
        return 0
    cache_key = (valve1, valve2, time, used)
    if cache_key in cache2:
        return cache2[cache_key]
    if_open1, idx1 = 0, 0
    if valve1 in with_flow:
        idx1 = with_flow.index(valve1)
        if used & (1 << idx1) == 0:
            if_open1 = flows[valve1] * (26 - time - 1)
    if_open2, idx2 = 0, 0
    if valve2 in with_flow and valve2 != valve1:
        idx2 = with_flow.index(valve2)
        if used & (1 << idx2) == 0:
            if_open2 = flows[valve2] * (26 - time - 1)
    moves1 = []
    if if_open1 > 0:
        moves1.append(valve1)
    for neigh in graph[valve1]:
        moves1.append(neigh)
    moves2 = []
    if if_open2 > 0:
        moves2.append(valve2)
    for neigh in graph[valve2]:
        moves2.append(neigh)

    best = 0
    for dest1 in moves1:
        for dest2 in moves2:
            gain = 0
            new_used = used
            if dest1 == valve1:
                gain += if_open1
                new_used |= 1 << idx1
            if dest2 == valve2:
                gain += if_open2
                new_used |= 1 << idx2
            sub = solve2(dest1, dest2, time + 1, new_used)
            best = max(best, sub + gain)

    cache2[cache_key] = best
    return best

res = solve2(ids['AA'], ids['AA'], 0, 0)
print(res)

# v, t, used, flow, sum = 0, 0, 0, 0, 0
# while t < 30:
#     sum += flow
#     _, use, neigh = cache[v][t][used]
#     if neigh == -1:
#         print(f'at time {t}, valve {v}, current flow is {flow}, total is {sum}')
#     else:
#         print(f'at time {t}, valve {v}, current flow is {flow}, {"" if use else " do not"} open it, the go to {neigh}')
#         if use:
#             t += 1
#             sum += flow
#             flow += flows[v]
#             used = used | (1 << (with_flow.index(v)))
#         v = neigh
#     t += 1
