import functools

res = 0
a, b = [], []

def cmp(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return -1 if a < b else (0 if a == b else 1)
    if isinstance(a, int):
        return cmp([a], b)
    if isinstance(b, int):
        return cmp(a, [b])
    nb_a, nb_b = len(a), len(b)
    for i in range(min(nb_a, nb_b)):
        c = cmp(a[i], b[i])
        if c != 0:
            return c
    return -1 if nb_a < nb_b else (0 if nb_a == nb_b else 1)

all = [[[2]],[[6]]]

i = 0
for line in open('test.in'):
    if i % 3 == 0:
        a = eval(line.rstrip())
        all.append(a)
    elif i % 3 == 1:
        b = eval(line.rstrip())
        all.append(b)
        if cmp(a, b) <= 0:
            res += i // 3 + 1
    i += 1

print(res)

all.sort(key=functools.cmp_to_key(cmp))
res = 1
for i in range(len(all)):
    if all[i] == [[2]] or all[i] == [[6]]:
        res *= i + 1

print(res)
