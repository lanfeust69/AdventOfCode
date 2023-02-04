serial = 9110

def power(x, y):
    p = ((x + 10) * y + serial) * (x + 10)
    return p // 100 % 10 - 5

grid = [[power(x, y) for x in range(1, 301)] for y in range(1, 301)]
cumul = [[0] * 300 for _ in range(300)]
for y in range(300):
    s = 0
    for x in range(300):
        s += grid[y][x]
        cumul[y][x] = s + (0 if y == 0 else cumul[y - 1][x])

def total(x, y, size):
    s = cumul[y + size - 1][x + size - 1]
    if x > 0:
        s -= cumul[y + size - 1][x - 1]
    if y > 0:
        s -= cumul[y - 1][x + size - 1]
    if x > 0 and y > 0:
        s += cumul[y - 1][x - 1]
    return s

best, x0, y0, best_size = 0, -1, -1, -1
for size in range(1, 301):
    for x in range(301 - size):
        for y in range(301 - size):
            s = total(x, y, size)
            if s > best:
                best, x0, y0, best_size = s, x, y, size

print(best, x0 + 1, y0 + 1, best_size)
