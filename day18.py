grid = [[c for c in line.rstrip()] for line in open('test.in')]

def step(grid):
    h, w = len(grid), len(grid[0])
    new_grid = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            nbs = {'|': 0, '.': 0, '#': 0}
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0:
                        continue
                    rr, cc = r + dr, c + dc
                    if rr >= 0 and rr < h and cc >= 0 and cc < w:
                        nbs[grid[rr][cc]] += 1
            if grid[r][c] == '.' and nbs['|'] >= 3:
                new_grid[r][c] = '|'
            elif grid[r][c] == '|' and nbs['#'] >= 3:
                new_grid[r][c] = '#'
            elif grid[r][c] == '#' and (nbs['|'] == 0 or nbs['#'] == 0):
                new_grid[r][c] = '.'
    return new_grid

def to_string(grid):
    return ''.join(''.join(row) for row in grid)

seen = [to_string(grid)]
seen_turn = {to_string(grid): 0}
target = 1000000000
found = False
for turn in range(target):
    grid = step(grid)
    changed = to_string(grid)
    if changed in seen:
        found = True
        print('cycle found at turn', turn)
        cycle = turn + 1 - seen_turn[changed]
        final_pos = seen_turn[changed] - 1 + (target - turn) % cycle
        final = seen[final_pos]
        nb_wood = sum(c == '|' for c in final)
        nb_lumber = sum(c == '#' for c in final)
        print(nb_wood, nb_lumber, nb_wood * nb_lumber)
        break
    seen.append(changed)
    seen_turn[changed] = turn + 1

if not found:
    nb_wood = sum(sum(c == '|' for c in row) for row in grid)
    nb_lumber = sum(sum(c == '#' for c in row) for row in grid)
    print(nb_wood, nb_lumber, nb_wood * nb_lumber)
