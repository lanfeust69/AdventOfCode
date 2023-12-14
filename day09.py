lines = [list(map(int, line.rstrip().split())) for line in open('test.in')]

res1, res2 = 0, 0
for line in lines:
    seq = []
    while any(line):
        seq.append(line[:])
        line = [line[i] - line[i - 1] for i in range(1, len(line))]
    v1, v2 = 0, 0
    for l in reversed(seq):
        v1 = l[-1] + v1
        v2 = l[0] - v2
    res1 += v1
    res2 += v2

print(res1)
print(res2)
