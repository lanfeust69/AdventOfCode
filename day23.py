elves = set()
r = 0
for line in open('test.in'):
    for c in range(len(line) - 1):
        if line[c] == '#':
            elves.add((r, c))
    r += 1

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

step = 0
while True:
    dests = {}
    for (r, c) in elves:
        possible = []
        for i in range(4):
            dr, dc = dirs[(i + step) % 4]
            ok = True
            if dc == 0:
                ok = all((r + dr, c + j) not in elves for j in range(-1, 2))
            else:
                ok = all((r + j, c + dc) not in elves for j in range(-1, 2))
            if ok:
                dest = r + dr, c + dc
                possible.append(dest)
        if 0 < len(possible) < 4:
            dest = possible[0]
            if dest in dests:
                dests[dest].append((r, c))
            else:
                dests[dest] = [(r, c)]

    if len(dests) == 0:
        print(step + 1)
        break

    for k, v in dests.items():
        if len(v) != 1:
            continue
        elves.remove(v[0])
        elves.add(k)

    if step == 9:
        min_r, max_r, min_c, max_c = 1000000, -1000000, 1000000, -1000000
        for r, c in elves:
            min_r = min(min_r, r)
            max_r = max(max_r, r)
            min_c = min(min_c, c)
            max_c = max(max_c, c)
        print((max_r - min_r + 1) * (max_c - min_c + 1) - len(elves))
    step += 1

# for r in range(min_r, max_r + 1):
#     line = ['#' if (r, c) in elves else '.' for c in range(min_c, max_c + 1)]
#     print(''.join(line))
# print('')
