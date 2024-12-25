edges = [tuple(line.rstrip().split('-')) for line in open('test.in')]
nodes = set([edge[0] for edge in edges] + [edge[1] for edge in edges])
graph = {node: set() for node in nodes}

for a, b in edges:
    graph[a].add(b)
    graph[b].add(a)

triplets = set()
for a, b in edges:
    for c in graph[a]:
        if c in graph[b]:
            triplets.add(tuple(sorted((a, b, c))))

print(len(triplets))
print(sum(any(name[0] == 't' for name in t) for t in triplets))

by_size = {}
largest_clique = set()

def bron_kerbosch(r, p, x):
    global largest_clique
    if len(p) == 0 and len(x) == 0:
        if len(r) in by_size:
            by_size[len(r)] += 1
        else:
            by_size[len(r)] = 1
        if len(r) > len(largest_clique):
            largest_clique = r
    else:
        while len(p):
            node = p.pop()
            bron_kerbosch(r | set([node]), p & graph[node], x & graph[node])
            x.add(node)

bron_kerbosch(set(), nodes, set())

print(by_size)
print(','.join(sorted(largest_clique)))
