from collections import Counter

ids = [line.rstrip() for line in open('test.in')]

nb2, nb3 = 0, 0
for id in ids:
    c = Counter(id)
    if 2 in c.values():
        nb2 += 1
    if 3 in c.values():
        nb3 += 1

print(nb2 * nb3)

for i in range(len(ids) - 1):
    for j in range(i + 1, len(ids)):
        diff = -1
        for k in range(len(ids[i])):
            if ids[i][k] == ids[j][k]:
                continue
            if diff != -1:
                diff = -1
                break
            diff = k
        if diff != -1:
            print(ids[i][:diff] + ids[i][diff + 1:])
