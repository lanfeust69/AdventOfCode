l1 = []
l2 = []

for line in open('test.in'):
    line = line.rstrip()
    (v1, v2) = map(int, line.split())
    l1.append(v1)
    l2.append(v2)

l1.sort()
l2.sort()

res = 0
for (v1, v2) in zip(l1, l2):
    res += abs(v1 - v2)

print(res)

freq = {}
for v in l2:
    if v in freq:
        freq[v] += 1
    else:
        freq[v] = 1

res = 0
for v in l1:
    if v in freq:
        res += v * freq[v]

print(res)
