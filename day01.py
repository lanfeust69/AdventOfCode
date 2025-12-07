pos = 50
res1 = 0
res2 = 0
for line in open('test.in'):
    line = line.rstrip()
    v = int(line[1:]) * [1, -1][line[0] == 'L']
    res2 += abs(v) // 100
    v = [v % 100, v % 100 - 100][v < 0]
    if (pos > 0 and pos + v <= 0) or pos + v >= 100:
        res2 += 1
    pos = (pos + v) % 100
    if pos == 0:
        res1 += 1
print(res1)
print(res2)
