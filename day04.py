grid = [[c == '@' for c in line.rstrip()] for line in open('test.in')]
h, w = len(grid), len(grid[0])

def available():
    res = []
    for r in range(h):
        for c in range(w):
            if not grid[r][c]:
                continue
            nb_neigh = sum(grid[r + dr][c + dc] for dr in range(-1, 2) for dc in range(-1, 2) if 0 <= r + dr < h and 0 <= c + dc < w) - 1
            if nb_neigh < 4:
                res.append((r, c))
    return res

todo = available()
part2 = len(todo)
print(len(todo))
nb_turn = 0
while todo:
    nb_turn += 1
    for (r, c) in todo:
        grid[r][c] = False
    todo = available()
    part2 += len(todo)

print(part2)
