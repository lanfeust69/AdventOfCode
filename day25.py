points = [tuple(map(int, line.rstrip().split(','))) for line in open('test.in')]

n = len(points)
graph = [[] for _ in range(n)]
for i in range(n - 1):
    for j in range(i + 1, n):
        d = sum(abs(points[i][k] - points[j][k]) for k in range(4))
        if d <= 3:
            graph[i].append(j)
            graph[j].append(i)

nb_comp = 0
seen = [False] * n
for i in range(n):
    if seen[i]:
        continue
    nb_comp += 1
    seen[i] = True
    todo = [i]
    while len(todo) > 0:
        next_todo = []
        for p in todo:
            for q in graph[p]:
                if seen[q]:
                    continue
                seen[q] = True
                next_todo.append(q)
        todo = next_todo

print(nb_comp)
