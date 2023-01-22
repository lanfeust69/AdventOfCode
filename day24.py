grid = []
row = 0
start = (0, 0)
waypoints = {}
for line in open('test.in'):
    line = line.rstrip()
    grid.append([c != '#' for c in line])
    for col in range(len(line)):
        if line[col] == '0':
            start = (row, col)
        elif line[col].isdigit():
            waypoints[(row, col)] = len(waypoints)
    row += 1

h, w = len(grid), len(grid[0])
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def neighbors(state):
    r, c, visited = state
    for dr, dc in dirs:
        rr, cc = r + dr, c + dc
        if rr < 0 or rr >= h or cc < 0 or cc >= w or not grid[rr][cc]:
            continue
        if (rr, cc) in waypoints:
            yield rr, cc, visited | (1 << waypoints[(rr, cc)])
        else:
            yield rr, cc, visited

all_visited = (1 << len(waypoints)) - 1
todo = [(*start, 0)]
seen = set(todo)
step = 0
while len(todo) > 0:
    step += 1
    next_todo = []
    for p in todo:
        for neigh in neighbors(p):
            # if neigh[2] == all_visited:
            if neigh[2] == all_visited and (neigh[0], neigh[1]) == start:
                print(step)
                exit(0)
            if neigh in seen:
                continue
            seen.add(neigh)
            next_todo.append(neigh)
    todo = next_todo
