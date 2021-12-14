for line in open('test.in'):
    positions = list(map(int, line.split(',')))
    break

def cost(pos):
    return sum(n * (n + 1) // 2 for n in (abs(x - pos) for x in positions))

inf, sup = min(positions), max(positions)
cur = (inf + sup) // 2
c0 = cost(cur)
c1 = cost(cur + 1)
if c1 < c0:
    c0 = c1
    cur += 2
    c = cost(cur)
    while c < c0:
        c0 = c
        cur += 1
        c = cost(cur)
else:
    c1 = cost(cur - 1)
    if c1 < c0:
        c0 = c1
        cur -= 2
        c = cost(cur)
        while c < c0:
            c0 = c
            cur -= 1
            c = cost(cur)

print(c0)
