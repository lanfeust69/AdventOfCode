deltas = [int(line.rstrip()) for line in open('test.in')]

print(sum(deltas))

pos = 0
f = 0
seen = set([0])
while True:
    f += deltas[pos]
    if f in seen:
        break
    seen.add(f)
    pos = (pos + 1) % len(deltas)

print(f)
