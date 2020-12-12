import sys
sys.stdin = open('test.in')

x, y = 0, 0
dx, dy = 10, 1
for line in sys.stdin:
    action = line[0]
    val = int(line[1:])
    if action == 'N':
        dy += val
    elif action == 'S':
        dy -= val
    elif action == 'E':
        dx += val
    elif action == 'W':
        dx -= val
    elif action == 'F':
        x += dx * val
        y += dy * val
    else:
        if action == 'R':
            val = 360 - val
        for _ in range(0, val // 90):
            dx, dy = -dy, dx

print(abs(x) + abs(y))

# x, y = 0, 0
# dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# curDir = 0
# dx, dy = dirs[curDir]
# for line in sys.stdin:
#     action = line[0]
#     val = int(line[1:])
#     if action == 'N':
#         y += val
#     elif action == 'S':
#         y -= val
#     elif action == 'E':
#         x += val
#     elif action == 'W':
#         x -= val
#     elif action == 'L':
#         curDir = (curDir + val // 90) % 4
#         dx, dy = dirs[curDir]
#     elif action == 'R':
#         curDir = (curDir + 4 - val // 90) % 4
#         dx, dy = dirs[curDir]
#     elif action == 'F':
#         x += dx * val
#         y += dy * val

# print(abs(x) + abs(y))
