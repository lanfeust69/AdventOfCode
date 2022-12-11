dirs = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
for line in open('test.in'):
    visited = set([(0, 0)])
    pos = [(0, 0), (0, 0)]
    idx = 0
    for c in line.rstrip():
        x, y = pos[idx % len(pos)]
        x += dirs[c][0]
        y += dirs[c][1]
        visited.add((x, y))
        pos[idx % len(pos)] = (x, y)
        idx += 1

    print(len(visited))
