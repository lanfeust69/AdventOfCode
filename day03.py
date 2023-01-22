target = 277678

n = 1
while (n + 2)**2 < target:
    n += 2
pos = (target - n**2 - 1) % (n + 1)
d = (n + 1) // 2 + abs(n // 2 - pos)
print(target, d)

grid = {(0, 0): 1, (1, 0): 1}
n, pos = 2, 0
v = 2
while True:
    pos += 1
    v += 1
    if pos == n * 4:
        n += 2
        pos = 0
    if pos // n == 0:
        x, y = n // 2, pos - n // 2 + 1
    elif pos // n == 1:
        x, y = n // 2 - 1 - pos % n, n // 2
    elif pos // n == 2:
        x, y = -n // 2, n // 2 - 1 - pos % n
    else:
        x, y = pos % n - n // 2 + 1, -n // 2
    s = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            xx, yy = x + dx, y + dy
            if (xx, yy) in grid:
                s += grid[(xx, yy)]
    if s > target:
        print(s)
        break
    grid[(x, y)] = s
