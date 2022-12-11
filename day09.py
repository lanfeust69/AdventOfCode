nb = 10
rope = [(0, 0)] * nb
dirs = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
visited = set([rope[-1]])
for line in open('test.in'):
    d, dist = line.split()
    dx, dy = dirs[d]
    for _ in range(int(dist)):
        rope[0] = rope[0][0] + dx, rope[0][1] + dy
        for i in range(1, nb):
            if abs(rope[i - 1][0] - rope[i][0]) < 2 and abs(rope[i - 1][1] - rope[i][1]) < 2:
                continue
            if rope[i - 1][0] == rope[i][0]:
                rope[i] = rope[i][0], rope[i][1] + (rope[i - 1][1] - rope[i][1]) // abs(rope[i - 1][1] - rope[i][1])
            elif rope[i - 1][1] == rope[i][1]:
                rope[i] = rope[i][0] + (rope[i - 1][0] - rope[i][0]) // abs(rope[i - 1][0] - rope[i][0]), rope[i][1]
            else:
                rope[i] = rope[i][0] + (rope[i - 1][0] - rope[i][0]) // abs(rope[i - 1][0] - rope[i][0]), rope[i][1] + (rope[i - 1][1] - rope[i][1]) // abs(rope[i - 1][1] - rope[i][1])
        visited.add(rope[-1])

print(len(visited))
