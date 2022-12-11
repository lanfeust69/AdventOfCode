part2 = True

grid = [[ord(c) - 97 for c in line.rstrip()] for line in open('test.in')]

h, w = len(grid), len(grid[0])
r0, c0, r1, c1 = -1, -1, -1, -1
for r in range(h):
    for c in range(w):
        if grid[r][c] == -14:
            r0, c0 = r, c
            grid[r][c] = 0
        elif grid[r][c] == -28:
            r1, c1 = r, c
            grid[r][c] = 25

def neighbors(p):
    r, c = p
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        rr, cc = r + dr, c + dc
        if rr >= 0 and rr < h and cc >= 0 and cc < w and grid[rr][cc] >= grid[r][c] - 1:
            yield rr, cc

visited = [[-1] * w for _ in range(h)]
visited[r1][c1] = 0
todo = [(r1, c1)]
dist = 0
found = False
while not found and len(todo) > 0:
    dist += 1
    next_todo = []
    for p in todo:
        for neigh in neighbors(p):
            if ((grid[neigh[0]][neigh[1]] == 0) if part2 else (neigh == (r0, c0))):
                found = True
                print(dist)
                break
            if visited[neigh[0]][neigh[1]] != -1:
                continue
            visited[neigh[0]][neigh[1]] = dist
            next_todo.append(neigh)
        if found:
            break
    todo = next_todo

if not found:
    print('not found...')
