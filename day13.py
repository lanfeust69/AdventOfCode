grid = [[c for c in line.rstrip()] for line in open('test.in')]
h, w = len(grid), max(len(r) for r in grid)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
corners = {'/': [1, 0, 3, 2], '\\': [3, 2, 1, 0]}
dir_names = '^>v<'
carts = []
carts_pos = {}

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] in dir_names:
            carts_pos[(r, c)] = len(carts)
            carts.append((r, c, dir_names.index(grid[r][c]), 0))
            grid[r][c] = '-' if grid[r][c] in '<>' else '|'

step = 0
first = True
crashed = set()
while True:
    step += 1
    to_delete = set()
    for i in sorted(range(len(carts)), key=lambda x: carts[x][0] * w + carts[x][1]):
        if i in crashed:
            continue
        r, c, d, t = carts[i]
        del carts_pos[(r, c)]
        dr, dc = dirs[d]
        r, c = r + dr, c + dc
        if (r, c) in carts_pos:
            if first:
                print('at step', step, 'crash at', f'{c},{r}')
                first = False
            crashed.add(carts_pos[(r, c)])
            crashed.add(i)
            to_delete.add((r, c))
        carts_pos[(r, c)] = i
        track = grid[r][c]
        if track in corners:
            d = corners[track][d]
        elif track == '+':
            d = (d - 1 + t % 3) % 4
            t += 1
        carts[i] = r, c, d, t
    for p in to_delete:
        del carts_pos[p]
    if len(crashed) == len(carts) - 1:
        break
    # for r in range(len(grid)):
    #     print(''.join(dir_names[carts[carts_pos[(r, c)]][2]] if (r, c) in carts_pos else grid[r][c] for c in range(len(grid[r]))))

for i in range(len(carts)):
    if i in crashed:
        continue
    r, c, _, _ = carts[i]
    print('at step', step, 'only one cart left, at', f'{c},{r}')
