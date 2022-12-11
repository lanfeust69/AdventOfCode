grid = [[c == '#' for c in line.rstrip()] for line in open('test.in')]

h, w = len(grid), len(grid[0])

grid[0][0] = grid[0][w - 1] = grid[h - 1][0] = grid[h - 1][w - 1] = True

def step(grid):
    new_grid = [[False] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            nb_neigh = 0
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0:
                        continue
                    rr, cc = r + dr, c + dc
                    if rr >= 0 and rr < h and cc >= 0 and cc < w and grid[rr][cc]:
                        nb_neigh += 1
            if nb_neigh == 3 or (nb_neigh == 2 and grid[r][c]):
                new_grid[r][c] = True
    new_grid[0][0] = new_grid[0][w - 1] = new_grid[h - 1][0] = new_grid[h - 1][w - 1] = True
    return new_grid

for _ in range(100):
    grid = step(grid)

print(sum(sum(row) for row in grid))
