places = {}
graph = []

for line in open('test.in'):
    p, d = line.rstrip().split(' = ')
    dist = int(d)
    a, b = p.split(' to ')
    if a in places:
        ida = places[a]
    else:
        ida = places[a] = len(places)
    if b in places:
        idb = places[b]
    else:
        idb = places[b] = len(places)
    while len(graph) < len(places):
        graph.append([])
    for g in graph:
        while len(g) < len(places):
            g.append(0)
    graph[ida][idb] = dist
    graph[idb][ida] = dist

print(graph)

nb_places = len(places)
nb_comb = 1 << nb_places
cache = [[-1] * nb_comb for _ in range(nb_places)]
minimize = False
def solve(node, used):
    if used == nb_comb - 1:
        return 0
    if cache[node][used] != -1:
        return cache[node][used]
    best = 10000 if minimize else 0
    for next_node in range(nb_places):
        if used & (1 << next_node):
            continue
        best = (min if minimize else max)(best, graph[node][next_node] + solve(next_node, used | (1 << next_node)))
    cache[node][used] = best
    return best

res = 10000 if minimize else 0
for start in range(len(graph)):
    res = (min if minimize else max)(res, solve(start, 1 << start))
print(res)
