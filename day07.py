res1, res2 = 0, 0

for line in open('test.in'):
    line = line.rstrip()
    lhs, rhs = line.split(': ')
    lhs = int(lhs)
    ops = list(map(int, rhs.split()))
    vals1 = set([ops[0]])
    vals2 = set([ops[0]])
    for i in range(1, len(ops)):
        new_vals1 = set()
        new_vals2 = set()
        for v in vals1:
            new_vals1.add(v + ops[i])
            new_vals1.add(v * ops[i])
        for v in vals2:
            new_vals2.add(v + ops[i])
            new_vals2.add(v * ops[i])
            new_vals2.add(int(str(v) + str(ops[i])))
        vals1 = new_vals1
        vals2 = new_vals2
    if lhs in vals1:
        res1 += lhs
    if lhs in vals2:
        res2 += lhs

print(res1)
print(res2)
