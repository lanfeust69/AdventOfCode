from typing import Counter

poly = ''
rules = {}
for line in open('test.in'):
    if len(line) < 2:
        continue
    p = line[:-1].split(' -> ')
    if len(p) == 1:
        poly = p[0]
    else:
        rules[p[0]] = p[1]

def expand(s):
    res = s[0]
    for i in range(1, len(s)):
        pattern = s[i - 1:i + 1]
        if pattern in rules:
            res += rules[pattern]
        res += s[i]
    return res

pairs = {}
for i in range(1, len(poly)):
    p = poly[i - 1:i + 1]
    if p in pairs:
        pairs[p] += 1
    else:
        pairs[p] = 1

for _ in range(40):
    new_pairs = {}
    for p in pairs:
        p1 = p[0] + rules[p]
        if p1 in new_pairs:
            new_pairs[p1] += pairs[p]
        else:
            new_pairs[p1] = pairs[p]
        p2 = rules[p] + p[1]
        if p2 in new_pairs:
            new_pairs[p2] += pairs[p]
        else:
            new_pairs[p2] = pairs[p]
    pairs = new_pairs
    # print(pairs)

counts = {c: 0 for c in 'OVSKPNFBCH'}
for p in pairs:
    counts[p[0]] += pairs[p]
    counts[p[1]] += pairs[p]
counts[poly[0]] += 1
counts[poly[-1]] += 1
print([(c, counts[c] // 2) for c in counts if counts[c] > 0])

print(max(counts.values()) // 2 - min(c for c in counts.values() if c > 0) // 2)
