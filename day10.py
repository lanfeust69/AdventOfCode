positions, speeds = [], []

for line in open('test.in'):
    p, v = (tuple(map(int, s[1:-1].split(', '))) for s in line.rstrip()[9:].split(' velocity='))
    positions.append(p)
    speeds.append(v)

# print(positions, speeds)

def display(positions):
    min_y = min(p[1] for p in positions)
    max_y = max(p[1] for p in positions)
    min_x = min(p[0] for p in positions)
    max_x = max(p[0] for p in positions)
    grid = [[' '] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for x, y in positions:
        grid[y - min_y][x - min_x] = '#'
    for row in grid:
        print(''.join(row))

prev = positions[:]
v_span = max(p[1] for p in positions) - min(p[1] for p in positions) + 1

t = 0
while True:
    min_y = min(p[1] for p in positions)
    max_y = max(p[1] for p in positions)
    if max_y - min_y + 1 > v_span:
        display(prev)
        break
    else:
        v_span = max_y - min_y + 1
    prev = positions[:]
    for i in range(len(positions)):
        positions[i] = (positions[i][0] + speeds[i][0], positions[i][1] + speeds[i][1])
    t += 1

print(t - 1)
