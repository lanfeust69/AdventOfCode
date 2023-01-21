import hashlib

seed = 'lpvhkcbi'

dirs = 'UDLR'
deltas = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def neighbors(x, y, path):
    h = hashlib.md5((seed + path).encode()).hexdigest()
    for dir in range(4):
        if h[dir] not in 'bcdef':
            continue
        xx, yy = x + deltas[dir][0], y + deltas[dir][1]
        if 0 <= xx < 4 and 0 <= yy < 4:
            yield xx, yy, path + dirs[dir]

start = (0, 0, '')
todo = [start]
shortest = ''
longest = 0
while len(todo) > 0:
    next_todo = []
    seen = set()
    for p in todo:
        for xx, yy, new_path in neighbors(*p):
            if new_path in seen:
                continue
            if xx == 3 and yy == 3:
                if not shortest:
                    shortest = new_path
                longest = len(new_path)
            else:
                seen.add(new_path)
                next_todo.append((xx, yy, new_path))
    todo = next_todo

print(shortest)
print(longest)
