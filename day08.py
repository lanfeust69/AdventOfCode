for line in open('test.in'):
    puzzle = list(map(int, line.rstrip().split()))

graph = []
metas = []

def parse(pos):
    id = len(graph)
    children = []
    graph.append(children)
    meta = []
    metas.append(meta)
    nb_children = puzzle[pos]
    nb_meta = puzzle[pos + 1]
    pos += 2
    for _ in range(nb_children):
        child_id, pos = parse(pos)
        children.append(child_id)
    metas[id] = puzzle[pos:pos + nb_meta]
    pos += nb_meta
    return id, pos

parse(0)
print(sum(sum(meta) for meta in metas))

values = [-1] * len(graph)

def val(node):
    if len(graph[node]) == 0:
        values[node] = sum(metas[node])
        return values[node]
    if values[node] != -1:
        return values[node]
    res = 0
    for i in metas[node]:
        if i <= len(graph[node]):
            res += val(graph[node][i - 1])
    values[node] = res
    return res

print(val(0))
