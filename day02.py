for line in open('test.in'):
    line = line.rstrip()
    ranges = [tuple(map(int, s.split('-'))) for s in line.split(',')]

def is_invalid(x, first_part):
    s = str(x)
    if len(s) < 2:
        return False
    if first_part and len(s) % 2 != 0:
        return False
    r = [len(s) // 2] if first_part else range(1, len(s) // 2 + 1)
    for l in r:
        if len(s) % l != 0:
            continue
        if all(s[i * l:(i + 1) * l] == s[:l] for i in range(1, len(s) // l)):
            return True
    return False

res1, nb1 = 0, 0
res2, nb2 = 0, 0
for (l, r) in ranges:
    for i in range(l, r + 1):
        if is_invalid(i, True):
            res1 += i
            nb1 += 1
        if is_invalid(i, False):
            res2 += i
            nb2 += 1
print(nb1, res1)
print(nb2, res2)
