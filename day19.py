first = True
patterns = []

for line in open('test.in'):
    line = line.rstrip()
    if first:
        available = line.split(', ')
        first = False
    elif len(line):
        patterns.append(line)

def solve(pattern):
    n = len(pattern)
    cache = [-1] * n
    def inner(pos):
        if pos == n:
            return 1
        if cache[pos] != -1:
            return cache[pos]
        res = 0
        for towel in available:
            if pos + len(towel) > n:
                continue
            if all(pattern[pos + i] == towel[i] for i in range(len(towel))):
                res += inner(pos + len(towel))
        cache[pos] = res
        return res
    return inner(0)

res1, res2 = 0, 0
for pattern in patterns:
    nb = solve(pattern)
    if nb:
        res1 += 1
    res2 += nb

print(res1)
print(res2)
