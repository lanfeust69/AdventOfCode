import sys
sys.stdin = open('test.in')

grid = [[]]
grid += [list('.' + l[:-1] + '.') for l in sys.stdin.readlines()]
width = len(grid[1])
grid[0] = ['.'] * width
grid.append(['.'] * width)

def occupied(grid, r, c, dr, dc):
    d = 1
    while r + dr * d >= 0 and r + dr * d < len(grid) and c + dc * d >= 0 and c + dc * d < width:
        if grid[r + dr * d][c + dc * d] == '#':
            return True
        if grid[r + dr * d][c + dc * d] == 'L':
            return False
        d += 1
    return False

changing = True
while changing:
    next_grid = [l[:] for l in grid]
    changing = False
    nb_occupied = 0
    for r in range(1, len(grid) - 1):
        for c in range(1, width - 1):
            if grid[r][c] == '.':
                continue
            nb_neigh = sum(1 for dr in range(-1, 2) for dc in range(-1, 2) if (dr != 0 or dc != 0) and occupied(grid, r, c, dr, dc))
            if grid[r][c] == 'L' and nb_neigh == 0:
                next_grid[r][c] = '#'
                nb_occupied += 1
                changing = True
            elif grid[r][c] == '#':
                if nb_neigh < 5:
                    nb_occupied += 1
                else:
                    next_grid[r][c] = 'L'
                    changing = True
    grid = next_grid

print(nb_occupied)
