grid = []
moves = ''
in_grid = True

for line in open('test.in'):
    line = line.rstrip()
    if not len(line):
        in_grid = False
        continue
    if in_grid:
        grid.append([c for c in line])
    else:
        moves += line

h, w = len(grid), len(grid[0])
r0, c0 = -1, -1
for r in range(h):
    for c in range(w):
        if grid[r][c] == '@':
            r0, c0 = r, c
            grid[r][c] = '.'
            break
    if r0 != -1:
        break

dir_syms = '^v<>'
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
r, c = r0, c0
grid2 = []
for row in grid:
    row2 = []
    for ch in row:
        if ch == '.':
            row2 += ['.', '.']
        elif ch == '#':
            row2 += ['#', '#']
        elif ch == 'O':
            row2 += ['[', ']']
    grid2.append(row2)

for move in moves:
    dr, dc = dirs[dir_syms.index(move)]
    rr, cc = r + dr, c + dc
    if grid[rr][cc] == '#':
        continue
    elif grid[rr][cc] == '.':
        r, c = rr, cc
        continue
    else:
        rs, cs = rr, cc
        while grid[rs][cs] == 'O':
            rs, cs = rs + dr, cs + dc
        if grid[rs][cs] == '#':
            continue
        else:
            grid[rs][cs] = 'O'
            grid[rr][cc] = '.'
            r, c = rr, cc

res = 0
for r in range(h):
    for c in range(w):
        if grid[r][c] == 'O':
            res += r * 100 + c

print(res)

w *= 2
grid = grid2
r, c = r0, c0 * 2
for move in moves:
    dr, dc = dirs[dir_syms.index(move)]
    rr, cc = r + dr, c + dc
    if grid[rr][cc] == '#':
        continue
    elif grid[rr][cc] == '.':
        r, c = rr, cc
        continue
    else:
        if move in '<>':
            rs, cs = rr, cc
            while grid[rs][cs] in '[]':
                rs, cs = rs + dr, cs + dc
            if grid[rs][cs] == '#':
                continue
            else:
                while cs != cc:
                    grid[rs][cs] = grid[rs][cs - dc]
                    cs -= dc
                grid[rr][cc] = '.'
                r, c = rr, cc
        else:
            moved = [(rr, cc) if grid[rr][cc] == '[' else (rr, cc - 1)]
            todo = moved[:]
            can_move = True
            while len(todo):
                new_todo = []
                for (rm, cm) in todo:
                    if grid[rm + dr][cm] == '#' or grid[rm + dr][cm + 1] == '#':
                        can_move = False
                        break
                    if grid[rm + dr][cm] == '[':
                        moved.append((rm + dr, cm))
                        new_todo.append((rm + dr, cm))
                    if grid[rm + dr][cm + 1] == '[':
                        moved.append((rm + dr, cm + 1))
                        new_todo.append((rm + dr, cm + 1))
                    if grid[rm + dr][cm] == ']':
                        moved.append((rm + dr, cm - 1))
                        new_todo.append((rm + dr, cm - 1))
                if not can_move:
                    break
                todo = new_todo
            if can_move:
                for rm, cm in reversed(moved):
                    grid[rm][cm] = '.'
                    grid[rm][cm + 1] = '.'
                    grid[rm + dr][cm] = '['
                    grid[rm + dr][cm + 1] = ']'
                r, c = rr, cc
grid[r][c] = '@'

res = 0
for r in range(h):
    for c in range(w):
        if grid[r][c] == '[':
            res += r * 100 + c

print(res)
for row in grid:
    print(''.join(row))
