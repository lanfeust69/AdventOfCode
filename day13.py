import math
import itertools

lines = [line.rstrip() for line in open('test.in')]
ids = {}
n = int(math.sqrt(len(lines))) + 1
happiness = [[0] * n for _ in range(n)]
for line in lines:
    parts = line[:-1].split() # remove final '.'
    a = parts[0]
    if a in ids:
        ida = ids[a]
    else:
        ida = ids[a] = len(ids)
    b = parts[-1]
    if b in ids:
        idb = ids[b]
    else:
        idb = ids[b] = len(ids)
    v = int(parts[3])
    if parts[2] == 'lose':
        v *= -1
    happiness[ida][idb] = v

best1 = -10000
for p in itertools.permutations(range(1, n)): # cycle : assume starting with 0
    score = happiness[0][p[0]] + happiness[0][p[-1]]
    for i in range(n - 1):
        score += happiness[p[i]][0] if i == 0 else happiness[p[i]][p[i - 1]]
        score += happiness[p[i]][0] if i == n - 2 else happiness[p[i]][p[i + 1]]
    best1 = max(best1, score)

print(best1)

best2 = -10000
for p in itertools.permutations(range(n)): # cycle : assume starting with me
    score = 0
    for i in range(n):
        score += 0 if i == 0 else happiness[p[i]][p[i - 1]]
        score += 0 if i == n - 1 else happiness[p[i]][p[i + 1]]
    best2 = max(best2, score)

print(best2)
