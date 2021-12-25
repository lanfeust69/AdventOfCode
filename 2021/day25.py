grid = [line[:-1] for line in open('test.in')]

h, w = len(grid), len(grid[0])

east, south = set(), set()

for r in range(h):
    for c in range(w):
        if grid[r][c] == '>':
            east.add((r, c))
        elif grid[r][c] == 'v':
            south.add((r, c))

progress = True
turn = 0
while progress:
    turn += 1
    if turn % 20 == 0:
        print('turn', turn)
    progress = False
    new_east = set()
    for r, c in east:
        dest = r, (c + 1) % w
        if dest not in east and dest not in south:
            progress = True
            new_east.add(dest)
        else:
            new_east.add((r, c))
    east = new_east
    new_south = set()
    for r, c in south:
        dest = (r + 1) % h, c
        if dest not in east and dest not in south:
            progress = True
            new_south.add(dest)
        else:
            new_south.add((r, c))
    south = new_south

print(turn)
