grid_done = False
grid = []
for line in open('test.in'):
    line = line.rstrip()
    if len(line) == 0:
        grid_done = True
    elif grid_done:
        path = line
    else:
        grid.append(line)

size = len(grid) // 3 if len(grid) % 3 == 0 else len(grid) // 4
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def move1(r, c, d):
    dr, dc = dirs[d]
    rr, cc = r + dr, c + dc
    while rr < 0 or rr >= len(grid) or cc < 0 or cc >= len(grid[rr]) or grid[rr][cc] == ' ':
        if rr < 0:
            rr = len(grid) - 1
        elif rr >= len(grid):
            rr = 0
        elif cc < 0:
            cc = len(grid[r]) - 1
        elif cc >= len(grid[r]):
            cc = 0
        else:
            rr, cc = rr + dr, cc + dc
    return rr, cc, d

#   T
# BLF
#   DR
def move2(r, c, d):
    dr, dc = dirs[d]
    rr, cc, dd = r + dr, c + dc, d
    if rr < 0 or rr >= size * 3 or cc < 0 or cc >= len(grid[rr]) or grid[rr][cc] == ' ':
        if rr < 0:
            rr, cc, dd = size, size * 3 - 1 - cc, 1
        elif rr >= size * 3:
            if cc < size * 3:
                rr, cc, dd = size * 2 - 1, size * 3 - 1 - cc, 3
            else:
                rr, cc, dd = size * 2 - 1 - (cc - size * 3), 0, 0
        elif cc < 0:
            rr, cc, dd = size * 3 - 1, size * 3 + (size * 2 - 1 - rr), 3
        elif cc >= len(grid[r]):
            if rr < size:
                rr, cc, dd = size * 2 + (size - 1 - rr), size * 4 - 1, 2
            elif rr < size * 2:
                rr, cc, dd = size * 2, size * 3 + (size * 2 - 1 - rr), 1
            else:
                rr, cc, dd = size - 1 - (rr - size * 2), size * 3 - 1, 2
        elif dc == -1:
            if rr < size:
                rr, cc, dd = size, size + rr, 1
            else:
                rr, cc, dd = size * 2 - 1, size * 2 - 1 - (rr - size * 2), 3
        elif r == size:
            if cc < size:
                rr, cc, dd = 0, size * 2 + (size - 1 - cc), 1
            else:
                rr, cc, dd = cc - size, size * 2, 0
        else:
            if cc < size:
                rr, cc, dd = size * 3 - 1, size * 2 + (size - 1 - cc), 3
            else:
                rr, cc, dd = size * 3 - 1 - (cc - size), size * 2, 0
    return rr, cc, dd

#  TR
#  F
# LD
# B
def move3(r, c, d):
    dr, dc = dirs[d]
    rr, cc, dd = r + dr, c + dc, d
    if rr < 0 or rr >= size * 4 or cc < 0 or cc >= len(grid[rr]) or grid[rr][cc] == ' ':
        if rr < 0:
            if cc < size * 2:
                rr, cc, dd = size * 2 + cc, 0, 0
            else:
                rr, cc, dd = size * 4 - 1, cc - size * 2, 3
        elif rr >= size * 4:
            rr, cc, dd = 0, size * 2 + cc, 1
        elif cc < 0:
            if rr < size * 3:
                rr, cc, dd = size - 1 - (rr - size * 2), size, 0
            else:
                rr, cc, dd = 0, size + (rr - size * 3), 1
        elif cc >= len(grid[rr]):
            if dc == 1:
                if rr < size:
                    rr, cc, dd = size * 2 + (size - 1 - rr), size * 2 - 1, 2
                elif rr < size * 2:
                    rr, cc, dd = size - 1, size * 2 + (rr - size), 3
                elif rr < size * 3:
                    rr, cc, dd = size * 3 - 1 - rr, size * 3 - 1, 2
                else:
                    rr, cc, dd = size * 3 - 1, size + (rr - size * 3), 3
            else:
                if rr == size:
                    rr, cc, dd = size + (cc - size * 2), size * 2 - 1, 2
                else:
                    rr, cc, dd = size * 3 + (cc - size), size - 1, 2
        elif dc == -1:
            if rr < size:
                rr, cc, dd = size * 2 + (size - 1 - rr), 0, 0
            else:
                rr, cc, dd = size * 2, rr - size, 1
        else:
            rr, cc, dd = size + c, size, 0
    return rr, cc, dd

r, c, d = 0, grid[0].index('.'), 0
# move = move1
# nasty : not same deployment for test and real !
move = move3 if size > 10 else move2
dist = 0
for ch in path + '#':
    if ch.isdigit():
        dist = dist * 10 + int(ch)
        continue
    for _ in range(dist):
        rr, cc, dd = move(r, c, d)
        if grid[rr][cc] == '#':
            break
        r, c, d = rr, cc, dd
    dist = 0
    if ch == 'R':
        d = (d + 1) % 4
    elif ch == 'L':
        d = (d + 3) % 4

print((r + 1) * 1000 + (c + 1) * 4 + d)
