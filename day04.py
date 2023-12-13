res1, res2 = 0, 0
pos = 0
copies = []
for line in open('test.in'):
    nb = 1 + sum(c[1] for c in copies)
    res2 += nb
    _, cards = line.rstrip().split(': ')
    winning, my = cards.split(' | ')
    winning = set([int(s) for s in winning.split() if s])
    my = set([int(s) for s in my.split() if s])
    c = len(winning & my)
    res1 += 0 if c == 0 else 2**(c - 1)
    copies = [(cc - 1, x) for (cc, x) in copies if cc > 1]
    if c > 0:
        copies.append((c, nb))

print(res1)
print(res2)
