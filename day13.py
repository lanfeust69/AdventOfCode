patterns = []
cur = []
for line in open('test.in'):
    line = line.rstrip()
    if line == '':
        patterns.append(cur)
        cur = []
        continue
    cur.append(line)
patterns.append(cur)

hsum1, vsum1 = 0, 0
hsum2, vsum2 = 0, 0
for pattern in patterns:
    h, w = len(pattern), len(pattern[0])
    for split in range(1, h):
        nb_fixed = 0
        for i in range(min(split, h - split)):
            nb_fixed += sum(pattern[split + i][c] != pattern[split - i - 1][c] for c in range(w))
            if nb_fixed > 1:
                break
        if nb_fixed == 0:
            hsum1 += split
        if nb_fixed == 1:
            hsum2 += split
    for split in range(1, w):
        nb_fixed = 0
        for i in range(min(split, w - split)):
            nb_fixed += sum(pattern[r][split + i] != pattern[r][split - i - 1] for r in range(h))
            if nb_fixed > 1:
                break
        if nb_fixed == 0:
            vsum1 += split
        if nb_fixed == 1:
            vsum2 += split

print(100 * hsum1 + vsum1)
print(100 * hsum2 + vsum2)
