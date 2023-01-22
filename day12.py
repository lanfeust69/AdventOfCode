graph = []
for line in open('test.in'):
    node, children = line.rstrip().split(' <-> ')
    node = int(node)
    while node >= len(graph):
        graph.append(None)
    graph[node] = list(map(int, children.split(', ')))

n = len(graph)

def dfs(node, seen):
    nb = 1
    for child in graph[node]:
        if not seen[child]:
            seen[child] = True
            nb += dfs(child, seen)
    return nb

seen = [False] * n
nb_components = 0
for node in range(n):
    if seen[node]:
        continue
    nb_components += 1
    seen[node] = True
    size = dfs(node, seen)
    if node == 0:
        print(size)

print(nb_components)
