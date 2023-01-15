res1, res2 = 0, 0
i = 0
lines = [[] for _ in range(3)]
for line in open('test.in'):
    ls = list(map(int, line.split()))
    lls = sorted(ls)
    if lls[-1] < lls[0] + lls[1]:
        res1 += 1
    lines[i] = ls
    if i == 2:
        for j in range(3):
            lls = sorted(lines[k][j] for k in range(3))
            if lls[-1] < lls[0] + lls[1]:
                res2 += 1
    i = (i + 1) % 3

print(res1, res2)
