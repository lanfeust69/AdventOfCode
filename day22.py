grid = []
prefix = '/dev/grid/node-'
for line in open('test.in'):
    if not line.startswith(prefix):
        continue
    tokens = line.rstrip().split()
    x, y = map(int, (s[1:] for s in tokens[0][len(prefix):].split('-')))
    while x >= len(grid):
        grid.append([])
    while y >= len(grid[x]):
        grid[x].append((0, 0, 0))
    grid[x][y] = tuple(map(int, (tokens[i][:-1] for i in range(1, 4))))

h, w = len(grid), len(grid[0])
nb_viable = 0
viable_dest = set()
min_size = 1000
max_under_empty = 0
for r0 in range(h):
    row = ''
    for c0 in range(w):
        min_size = min(min_size, grid[r0][c0][0])
        if grid[r0][c0][1] <= 94:
            max_under_empty = max(max_under_empty, grid[r0][c0][1])
            row += ' ' if grid[r0][c0][1] == 0 else '.'
        else:
            row += '#'
            # print(r0, c0, grid[r0][c0])
        for r1 in range(h):
            for c1 in range(w):
                if r0 == r1 and c0 == c1:
                    continue
                if grid[r0][c0][1] != 0 and grid[r0][c0][1] <= grid[r1][c1][2]:
                    nb_viable += 1
                    viable_dest.add((r1, c1))
    print(row)

print(nb_viable)
print(viable_dest)
print(min_size, max_under_empty)

print(4 + 25 + 28 + 28 * 5 + 1)