file = open('test.in')

y = 0
state = set()
for line in file:
    for x, c in enumerate(line):
        if c == '#':
            state.add((x, y, 0, 0))
    y += 1

def get_neighbors(p):
    x, y, z, w = p
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                        continue
                    yield x + dx, y + dy, z + dz, w + dw

for _ in range(6):
    next_state = set()
    can_appear = {}
    for alive in state:
        nb_neighbors = 0
        for neighbor in get_neighbors(alive):
            if neighbor in state:
                nb_neighbors += 1
            else:
                can_appear[neighbor] = can_appear.get(neighbor, 0) + 1
        if nb_neighbors == 2 or nb_neighbors == 3:
            next_state.add(alive)
    for p, nb in can_appear.items():
        if nb == 3:
            next_state.add(p)
    state = next_state

print(len(state))
