import re, math

file = open('test.in')

tiles = {}
cur_id = 0
cur_tile = []
for line in file:
    m = re.match(r'Tile (\d+):', line)
    if m:
        if len(cur_tile) > 0:
            tiles[cur_id] = cur_tile
            cur_tile = []
        cur_id = m.group(1)
        continue
    if len(line) > 1:
        cur_tile.append(line[:-1])
tiles[cur_id] = cur_tile
tile_size = len(cur_tile)

# tranform is 0-7 for id, r90, r180, r270, fv, fh, fd, fc
# side is 0-3 for top, right, bottom, left
# result is always left to right or top to bottom
def border(tile, transform, side):
    if (transform, side) in [(0, 0), (1, 1), (4, 2), (7, 3)]:
        return tile[0]
    if (transform, side) in [(5, 0), (6, 1), (2, 2), (3, 3)]:
        return ''.join(reversed(tile[0]))
    if (transform, side) in [(3, 0), (0, 1), (7, 2), (5, 3)]:
        return ''.join(l[-1] for l in tile)
    if (transform, side) in [(6, 0), (4, 1), (1, 2), (2, 3)]:
        return ''.join(reversed([l[-1] for l in tile]))
    if (transform, side) in [(4, 0), (7, 1), (0, 2), (1, 3)]:
        return tile[-1]
    if (transform, side) in [(2, 0), (3, 1), (5, 2), (6, 3)]:
        return ''.join(reversed(tile[-1]))
    if (transform, side) in [(7, 0), (5, 1), (3, 2), (0, 3)]:
        return ''.join(l[0] for l in tile)
    if (transform, side) in [(1, 0), (2, 1), (6, 2), (4, 3)]:
        return ''.join(reversed([l[0] for l in tile]))

def cell(tile, transform, row, col):
    n0 = len(tile) - 1
    n1 = len(tile[0]) - 1
    if transform == 0:
        return tile[row][col]
    if transform == 1:
        return tile[n0 - col][row]
    if transform == 2:
        return tile[n0 - row][n1 - col]
    if transform == 3:
        return tile[col][n1 - row]
    if transform == 4:
        return tile[n0 - row][col]
    if transform == 5:
        return tile[row][n1 - col]
    if transform == 6:
        return tile[n0 - col][n1 - row]
    if transform == 7:
        return tile[col][row]

# for each border : the list of (tiles, transform) that have this border as top line
rev_transforms = [0, 3, 2, 1, 4, 5, 6, 7]
comp_by_fc = [7, 4, 6, 5, 1, 3, 2, 0]
tiles_by_border = {}
def add_by_border(key, val):
    global tiles_by_border
    if key in tiles_by_border:
        tiles_by_border[key].append(val)
    else:
        tiles_by_border[key] = [val]
for id, tile in tiles.items():
    for transform in range(8):
        add_by_border(border(tile, transform, 0), (id, transform))

size = int(math.sqrt(len(tiles)))
assembled = [[None] * size for _ in range(size)]

def assemble(row, col, available):
    global assembled
    if row == size:
        return True
    next_row, next_col = (row, col + 1) if col < size - 1 else (row + 1, 0)
    candidates = set((id, t) for t in range(8) for id in available)
    if col > 0:
        candidates.intersection_update((t[0], comp_by_fc[t[1]]) for t in tiles_by_border[assembled[row][col - 1][1]])
    if row > 0:
        candidates.intersection_update(tiles_by_border[assembled[row - 1][col][2]])
    for candidate in candidates:
        assembled[row][col] = (candidate, border(tiles[candidate[0]], candidate[1], 1), border(tiles[candidate[0]], candidate[1], 2))
        available.remove(candidate[0])
        if assemble(next_row, next_col, available):
            return True
        available.add(candidate[0])
    return False

ok = assemble(0, 0, set(tiles))
assert ok
corners = [int(assembled[r][c][0][0]) for r, c in [(0, 0), (0, size - 1), (size - 1, 0), (size - 1, size - 1)]]
res = 1
for id in corners:
    res *= id
print(res)

image_size = size * (tile_size - 2)
image = [[' '] * image_size for _ in range(image_size)]
for r in range(size):
    for c in range(size):
        id, transform = assembled[r][c][0]
        for rr in range(tile_size - 2):
            for cc in range(tile_size - 2):
                image[r * (tile_size - 2) + rr][c * (tile_size - 2) + cc] = cell(tiles[id], transform, rr + 1, cc + 1)

for l in image:
    print(''.join(l))

monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ']
monsters_h = [set((r, c) for r in range(len(monster)) for c in range(len(monster[0])) if cell(monster, t, r, c) == '#') for t in [0, 2, 4, 5]]
monsters_v = [set((r, c) for r in range(len(monster[0])) for c in range(len(monster)) if cell(monster, t, r, c) == '#') for t in [1, 3, 6, 7]]

total = sum(sum(1 for c in image[row] if c == '#') for row in range(image_size))
in_monster = set()
for row in range(image_size - len(monster)):
    for col in range(image_size - len(monster[0])):
        for m in monsters_h:
            if all(image[row + dr][col + dc] == '#' for dr, dc in m):
                for dr, dc in m:
                    in_monster.add((row + dr, col + dc))
for row in range(image_size - len(monster[0])):
    for col in range(image_size - len(monster)):
        for m in monsters_v:
            if all(image[row + dr][col + dc] == '#' for dr, dc in m):
                for dr, dc in m:
                    in_monster.add((row + dr, col + dc))

print(total - len(in_monster))
