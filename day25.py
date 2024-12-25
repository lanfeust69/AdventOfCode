lines = [line.rstrip() for line in open('test.in')]

locks, keys = [], []
i = 0
while i * 8 + 6 < len(lines):
    is_key = lines[i * 8] == '.' * 5
    counts = [0] * 5
    for j in range(5):
        for k in range(5):
            if lines[i * 8 + 1 + j][k] == '#':
                counts[k] += 1
    if is_key:
        keys.append(counts)
    else:
        locks.append(counts)
    i += 1

res = 0
for lock in locks:
    for key in keys:
        if all(lock[i] + key[i] <= 5 for i in range(5)):
            res += 1

print(res)
