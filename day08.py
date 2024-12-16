r = 0
w = 0
antennas = {}
for line in open('test.in'):
    line = line.rstrip()
    if w == 0:
        w = len(line)
    for c in range(w):
        if line[c] == '.':
            continue
        if line[c] in antennas:
            antennas[line[c]].append((r, c))
        else:
            antennas[line[c]] = [(r, c)]
    r += 1
h = r

anti_nodes = set()
anti_nodes2 = set()
for (_, lst) in antennas.items():
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            r, c = lst[j][0] * 2 - lst[i][0], lst[j][1] * 2 - lst[i][1]
            if 0 <= r < h and 0 <= c < w:
                anti_nodes.add((r, c))
            r, c = lst[i]
            dr, dc = lst[j][0] - lst[i][0], lst[j][1] - lst[i][1]
            while True:
                r, c = r + dr, c + dc
                if not (0 <= r < h and 0 <= c < w):
                    break
                anti_nodes2.add((r, c))

print(len(anti_nodes))
print(len(anti_nodes2))
