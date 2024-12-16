deps = {}
updates = []

for line in open('test.in'):
    line = line.rstrip()
    if '|' in line:
        a, b = map(int, line.split('|'))
        if b in deps:
            deps[b].append(a)
        else:
            deps[b] = [a]
        if a not in deps:
            deps[a] = []
    elif ',' in line:
        updates.append(list(map(int, line.split(','))))

print(len(deps), 'nodes')
visited = {x: False for x in deps}
def dfs(node):
    for child in deps[node]:
        if not visited[child]:
            visited[child] = True
            return dfs(child) + [node]
    return []
for node in deps:
    cycle = dfs(node)
    print('cycle of len', len(cycle))
    break

res1 = 0
res2 = 0
for update in updates:
    ok = True
    for i in range(len(update) - 1):
        a = update[i]
        a_dep = deps[a]
        for j in range(i + 1, len(update)):
            if update[j] in a_dep:
                ok = False
                break
        if not ok:
            break
    if ok:
        res1 += update[len(update) // 2]
    else:
        for i in range(len(update) - 1):
            for j in range(i + 1, len(update)):
                if update[j] in deps[update[i]]:
                    update[i], update[j] = update[j], update[i]
        res2 += update[len(update) // 2]

print(res1)
print(res2)
