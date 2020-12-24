def to_coord(s):
    x, y = 0, 0
    while len(s) > 0:
        if s[0] == 'e':
            x += 1
            s = s[1:]
        elif s[0] == 'w':
            x -= 1
            s = s[1:]
        elif s[0:2] == 'ne':
            y += 1
            s = s[2:]
        elif s[0:2] == 'nw':
            x -= 1
            y += 1
            s = s[2:]
        elif s[0:2] == 'se':
            x += 1
            y -= 1
            s = s[2:]
        elif s[0:2] == 'sw':
            y -= 1
            s = s[2:]
        else:
            assert False
    return x, y

tiles = {}
for line in open('test.in'):
    p = to_coord(line[:-1])
    tiles[p] = tiles.get(p, False) ^ True

print(sum(1 for _, v in tiles.items() if v))

def get_neighbors(p):
    x, y = p
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]:
        yield x + dx, y + dy

black_tiles = set(p for p, v in tiles.items() if v)
for step in range(100):
    new_black = set()
    can_turn_black = {}
    for p in black_tiles:
        nb = 0
        for neigh in get_neighbors(p):
            if neigh in black_tiles:
                nb += 1
            else:
                can_turn_black[neigh] = can_turn_black.get(neigh, 0) + 1
        if nb in [1, 2]:
            new_black.add(p)
    new_black.update(p for p, n in can_turn_black.items() if n == 2)
    black_tiles = new_black

print(len(black_tiles))
