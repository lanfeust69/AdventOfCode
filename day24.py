grid = [line.rstrip() for line in open('test.in')]

h, w = len(grid), len(grid[0])
start = (0, grid[0].index('.'))
exit_c = grid[h - 1].index('.')

reachable = set([start])
exit_target = (h - 2, exit_c)
target = exit_target
first = True
t = 0
while len(reachable) > 0:
    t += 1
    inside_allowed = [[True] * (w - 2) for _ in range(h - 2)]
    for r in range(h - 2):
        for c in range(w - 2):
            wind = grid[r + 1][c + 1]
            if wind == '>':
                inside_allowed[r][(c + t) % (w - 2)] = False
            elif wind == '<':
                inside_allowed[r][(c - t) % (w - 2)] = False
            elif wind == 'v':
                inside_allowed[(r + t) % (h - 2)][c] = False
            elif wind == '^':
                inside_allowed[(r - t) % (h - 2)][c] = False
    new_reachable = set()
    for r, c in reachable:
        if (r, c) == target:
            print(t)
            if target == exit_target:
                if first:
                    new_reachable = set([(h - 1, exit_c)])
                    target = (1, start[1])
                    first = False
                else:
                    exit(0)
            else:
                new_reachable = set([start])
                target = exit_target
            break
        if r == 0 or r == h - 1 or inside_allowed[r - 1][c - 1]:
            new_reachable.add((r, c)) # wait
        if r < h - 2 and inside_allowed[r][c - 1]:
            new_reachable.add((r + 1, c))
        if r > 1 and inside_allowed[r - 2][c - 1]:
            new_reachable.add((r - 1, c))
        if r > 0 and r < h - 1 and c < w - 2 and inside_allowed[r - 1][c]:
            new_reachable.add((r, c + 1))
        if r > 0 and r < h - 1 and c > 1 and inside_allowed[r - 1][c - 2]:
            new_reachable.add((r, c - 1))
    reachable = new_reachable
    if t % 50 == 0:
        print(len(reachable), 'reachable at time', t)

print('not found...')
