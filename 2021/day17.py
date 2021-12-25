import math

# x_min, x_max, y_min, y_max = 20, 30, -10, -5
x_min, x_max, y_min, y_max = 14, 50, -267, -225

res = 0

for dx0 in range(x_max + 1):
    if dx0 * (dx0 + 1) // 2 < x_min:
        continue
    for dy0 in range(y_min, -y_min):
        x, y = 0, 0
        dx, dy = dx0, dy0
        while True:
            if x > x_max or y < y_min:
                break
            if x_min <= x <= x_max and y_min <= y <= y_max:
                res += 1
                break
            x += dx
            if dx > 0:
                dx -= 1
            y += dy
            dy -= 1

print(res)
