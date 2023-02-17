for line in open('test.in'):
    puzzle = line.rstrip()

graph = {}
stack = [(0, 0)]
dirs = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
for c in puzzle[1:-1]:
    if c in dirs:
        src = stack[-1]
        dest = tuple(src[i] + dirs[c][i] for i in range(2))
        if src in graph:
            graph[src].append(dest)
        else:
            graph[src] = [dest]
        if dest in graph:
            graph[dest].append(src)
        else:
            graph[dest] = [src]
        stack[-1] = dest
        continue
    if c == '(':
        stack.append(stack[-1])
    elif c == '|':
        stack.pop()
        stack.append(stack[-1])
    elif c == ')':
        stack.pop()

print(len(graph))
min_x = min(p[0] for p in graph)
max_x = max(p[0] for p in graph)
min_y = min(p[1] for p in graph)
max_y = max(p[1] for p in graph)
h = (max_y - min_y + 1) * 2 + 1
w = (max_x - min_x + 1) * 2 + 1
grid = [['#'] * w for _ in range(h)]
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        if (x, y) not in graph:
            print((x, y), 'not in graph !')
            continue
        r = (max_y - y) * 2 + 1
        c = (x - min_x) * 2 + 1
        grid[r][c] = ' ' if x != 0 or y != 0 else 'X'
        if (x, y + 1) in graph[(x, y)]:
            grid[r - 1][c] = '-'
        if (x, y - 1) in graph[(x, y)]:
            grid[r + 1][c] = '-'
        if (x + 1, y) in graph[(x, y)]:
            grid[r][c + 1] = '|'
        if (x - 1, y) in graph[(x, y)]:
            grid[r][c - 1] = '|'

# for row in grid:
#     print(''.join(row))

seen = set([(0, 0)])
part2 = 0
todo = [(0, 0)]
dist = 0
while len(todo) > 0:
    dist += 1
    next_todo = []
    for p in todo:
        for neigh in graph[p]:
            if neigh in seen:
                continue
            seen.add(neigh)
            if dist >= 1000:
                part2 += 1
            next_todo.append(neigh)
    todo = next_todo

print(dist - 1)
print(part2)
