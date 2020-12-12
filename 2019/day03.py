file = open('test.in')
path1 = file.readline().split(',')
path2 = file.readline().split(',')
# path1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
# path2 = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')

visited = {}
dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
x, y = 0, 0
step = 0
for move in path1:
    dx, dy = dirs[move[0]]
    val = int(move[1:])
    for _ in range(val):
        step += 1
        x, y = x + dx, y + dy
        if (x, y) not in visited:
            visited[(x, y)] = step

x, y = 0, 0
step = 0
best = 1000000000
for move in path2:
    dx, dy = dirs[move[0]]
    val = int(move[1:])
    for _ in range(val):
        step += 1
        x, y = x + dx, y + dy
        if (x, y) in visited:
            best = min(best, step + visited[(x, y)])
            del visited[(x, y)]

print(best)
