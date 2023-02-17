points = set()
min_x, max_x, min_y, max_y = 1000000, 0, 1000000, 0
for line in open('test.in'):
    a, b = line.rstrip().split(', ')
    l, r = map(int, b[2:].split('..'))
    if a[0] == 'x':
        xs = [int(a[2:])]
        ys = list(range(l, r + 1))
    else:
        ys = [int(a[2:])]
        xs = list(range(l, r + 1))
    min_x = min(min_x, xs[0])
    max_x = max(max_x, xs[-1])
    min_y = min(min_y, ys[0])
    max_y = max(max_y, ys[-1])
    for x in xs:
        for y in ys:
            points.add((x, y))

original_points = set(points)

reachable = [set() for _ in range(max_y + 1)]
reachable[0].add(500)
todo = set([(500, 0)])
res = 0

while len(todo) > 0:
    next_todo = set()
    for x, y in todo:
        if y == max_y:
            continue
        if (x, y) in points:
            continue # already filled
        if (x, y + 1) not in points:
            reachable[y + 1].add(x)
            next_todo.add((x, y + 1))
        else:
            x_right = x
            closed_right = False
            while True:
                if (x_right + 1, y) in points:
                    closed_right = True
                    break
                x_right += 1
                if (x_right, y + 1) not in points:
                    break
            x_left = x
            closed_left = False
            while True:
                if (x_left - 1, y) in points:
                    closed_left = True
                    break
                x_left -= 1
                if (x_left, y + 1) not in points:
                    break
            if closed_left and closed_right:
                for xx in range(x_left, x_right + 1):
                    points.add((xx, y))
                    reachable[y].discard(xx)
                    res += 1
                for xx in reachable[y - 1]:
                    if x_left <= xx <= x_right:
                        next_todo.add((xx, y - 1))
            else:
                for xx in range(x_left, x_right + 1):
                    reachable[y].add(xx)
                if not closed_left:
                    next_todo.add((x_left, y))
                if not closed_right:
                    next_todo.add((x_right, y))
    todo = next_todo

print(res + sum(len(r) for r in reachable[min_y:]))
print(res)

# print('#' * (max_x - min_x + 1))
# for y in range(max_y + 1):
#     print(''.join('|' if x in reachable[y] else ('#' if (x, y) in original_points else ('~' if (x, y) in points else ' ')) for x in range(min_x, max_x + 2)))
