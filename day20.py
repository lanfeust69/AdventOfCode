def parse(line):
    return tuple(tuple(map(int, s[3:-1].split(','))) for s in line.split(', '))

ps = [parse(line.rstrip()) for line in open('test.in')]

candidates = []
slowest = 1000

for i in range(len(ps)):
    _, _, (ax, ay, az) = ps[i]
    a = ax * ax + ay * ay + az * az
    if a < slowest:
        candidates = [i]
        slowest = a
    elif a == slowest:
        candidates.append(i)

print(candidates)
print([ps[i] for i in candidates])

in_fly = set(range(len(ps)))
nb_escaped = 0

# could try to identify escaped particles :
# along each axis : fastest acceleration, that are already faster and further than all others
time_without = 0
t = 0
while len(in_fly) > 0 and time_without < 1000:
    time_without += 1
    t += 1
    positions = {}
    for i in in_fly:
        p = ps[i]
        x, y, z = [p[0][j] + t * p[1][j] + t * (t + 1) * p[2][j] // 2  for j in range(3)]
        if (x, y, z) in positions:
            positions[(x, y, z)].append(i)
        else:
            positions[(x, y, z)] = [i]
    for colliding in positions.values():
        if len(colliding) > 1:
            time_without = 0
            for i in colliding:
                in_fly.remove(i)

print(len(in_fly))
