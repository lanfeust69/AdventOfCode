grid = [[c for c in line.rstrip()] for line in open('test.in')]

h, w = len(grid), len(grid[0])

def display():
    for row in grid:
        print(''.join(row))

def neighbors(r, c):
    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]: # sorted in reading order
        rr, cc = r + dr, c + dc
        if grid[rr][cc] != '#':
            yield rr, cc

def play(grid, elf_attack):
    def is_in_range(u, r, c):
        for rr, cc in neighbors(r, c):
            if grid[rr][cc] == u:
                return True
        return False
    units = {}
    for r in range(h):
        for c in range(w):
            if grid[r][c] in 'EG':
                units[(r, c)] = (grid[r][c], 200)
    nb_elves = sum(u[0] == 'E' for u in units.values())
    nb_goblins = len(units) - nb_elves
    round = 0
    last_round_full = True
    elf_killed = False
    while nb_elves > 0 and nb_goblins > 0:
        round += 1
        killed = set()
        for r, c in sorted(units.keys()):
            if (r, c) in killed:
                continue
            u, hp = units[(r, c)]
            if (u == 'G' and nb_elves == 0) or (u == 'E' and nb_goblins == 0):
                last_round_full = False
            opp, attack = ('G', elf_attack) if u == 'E' else ('E', 3)
            if not is_in_range(opp, r, c):
                # move
                parents = {(r, c): (r, c)}
                todo = [(r, c)]
                targets = []
                while len(targets) == 0 and len(todo) > 0:
                    next_todo = []
                    for p in todo:
                        for n in neighbors(*p):
                            if n in parents or grid[n[0]][n[1]] != '.':
                                continue
                            parents[n] = p
                            if is_in_range(opp, *n):
                                targets.append(n)
                            next_todo.append(n)
                    todo = sorted(next_todo)
                if len(targets) > 0:
                    targets.sort()
                    target = targets[0]
                    while parents[target] != (r, c):
                        target = parents[target]
                    grid[target[0]][target[1]] = u
                    units[target] = u, hp
                    grid[r][c] = '.'
                    del units[(r, c)]
                    r, c = target
            if is_in_range(opp, r, c):
                target_hp = 1000
                target = (-1, -1)
                for rr, cc in neighbors(r, c):
                    if grid[rr][cc] == opp and units[(rr, cc)][1] < target_hp:
                        target = (rr, cc)
                        target_hp = units[target][1]
                if target_hp <= attack:
                    killed.add(target)
                    del units[target]
                    if opp == 'E':
                        nb_elves -= 1
                        elf_killed = True
                    else:
                        nb_goblins -= 1
                    grid[target[0]][target[1]] = '.'
                else:
                    units[target] = (opp, target_hp - attack)
        # display()
    if not last_round_full:
        round -= 1
    survivors = sum(u[1] for u in units.values())
    return elf_killed, round, survivors

_, round, survivors = play([row[:] for row in grid], 3)
print(round, survivors, round * survivors)

inf, sup = 3, 200
while inf < sup - 1:
    mid = (inf + sup) // 2
    ko, r, s = play([row[:] for row in grid], mid)
    if ko:
        inf = mid
    else:
        sup = mid
        round, survivors = r, s

print(sup, round, survivors, round * survivors)
# 54680 too low, 56047 too high
# for a in range(4, 50):
#     print(play([row[:] for row in grid], a))
