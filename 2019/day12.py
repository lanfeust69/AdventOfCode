file = open('test.in')

moons = []
for line in file:
    coords = [int(l[2:]) for l in line[1:-2].split(', ')]
    moons.append((coords, [0, 0, 0]))

def step(moons):
    for i in range(len(moons) - 1):
        for j in range(i + 1, len(moons)):
            for coord in range(3):
                if moons[i][0][coord] == moons[j][0][coord]:
                    continue
                if moons[i][0][coord] < moons[j][0][coord]:
                    moons[i][1][coord] += 1
                    moons[j][1][coord] -= 1
                else:
                    moons[i][1][coord] -= 1
                    moons[j][1][coord] += 1
    for i in range(len(moons)):
        moons[i] = ([moons[i][0][coord] + moons[i][1][coord] for coord in range(3)], moons[i][1])

def energy(moons):
    return sum(sum(abs(x) for x in moon[0]) * sum(abs(x) for x in moon[1]) for moon in moons)

res = []
def key(moons, coord):
    return tuple([(moon[0][coord], moon[1][coord]) for moon in moons])

cycles = []
for coord in range(3):
    cur = 0
    to_step = [(moon[0][:], moon[1][:]) for moon in moons]
    seen = {key(to_step, coord): cur}
    while True:
        cur += 1
        step(to_step)
        new_key = key(to_step, coord)
        if new_key in seen:
            assert(seen[new_key] == 0)
            cycles.append(cur)
            break
        seen[new_key] = cur

def gcd(a, b): return a if b == 0 else gcd(b, a % b)
lcm = 1
for cycle in cycles:
    lcm = lcm * cycle // gcd(lcm, cycle)

print(lcm)
