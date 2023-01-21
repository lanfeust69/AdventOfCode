n = 1350

cache = {}

def is_open(x, y):
    if x < 0 or y < 0:
        return False
    if (x, y) in cache:
        return cache[(x, y)]
    s = (x + y)**2 + 3 * x + y + n
    nb_set = 0
    while s > 0:
        if s & 1:
            nb_set += 1
        s >>= 1
    res = nb_set % 2 == 0
    cache[(x, y)] = res
    return res

dest = (31, 39)
todo = [(1, 1)]
seen = set(todo)
step = 0

# while len(todo) > 0:
while step < 50:
    step += 1
    next_todo = []
    for x, y in todo:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xx, yy = x + dx, y + dy
            # if (xx, yy) == dest:
            #     print(step)
            #     exit(0)
            if is_open(xx, yy) and (xx, yy) not in seen:
                next_todo.append((xx, yy))
                seen.add((xx, yy))
    todo = next_todo

print(len(seen))
