grid = [[int(c) for c in line[:-1]] for line in open('test.in')]
h, w = len(grid), len(grid[0])

def neighbors(r, c):
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            rr, cc = r + dr, c + dc
            if rr >= 0 and rr < h and cc >= 0 and cc < w:
                yield (rr, cc)

def step():
    todo = []
    nb_flash = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 9:
                nb_flash += 1
                grid[r][c] = 0
                todo.append((r, c))
            else:
                grid[r][c] += 1
    while len(todo) > 0:
        next_todo = []
        for r, c in todo:
            for rr, cc in neighbors(r, c):
                if grid[rr][cc] == 0:
                    continue
                if grid[rr][cc] == 9:
                    nb_flash += 1
                    grid[rr][cc] = 0
                    next_todo.append((rr, cc))
                else:
                    grid[rr][cc] += 1
        todo = next_todo
    return nb_flash

time = 0
while True:
    time += 1
    if step() == h * w:
        break

print(time)
