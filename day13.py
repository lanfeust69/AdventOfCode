ranges = []
for line in open('test.in'):
    pos, r = map(int, line.rstrip().split(': '))
    while pos >= len(ranges):
        ranges.append(0)
    ranges[pos] = r

n = len(ranges)
sev = 0

for i in range(n):
    if ranges[i] and (ranges[i] == 1 or i % ((ranges[i] - 1) * 2) == 0):
        sev += i * ranges[i]

print(sev)

wait = 0
while True:
    ok = True
    for i in range(n):
        if ranges[i] and (ranges[i] == 1 or (i + wait) % ((ranges[i] - 1) * 2) == 0):
            ok = False
            break
    if ok:
        break
    wait += 1

print(wait)
