counts = [0] * 9
for line in open('test.in'):
    for i in map(int, line.split(',')):
        counts[i] += 1

for _ in range(256):
    n0 = counts[0]
    for i in range(1, 9):
        counts[i - 1] = counts[i]
    counts[6] += n0
    counts[8] = n0

print(sum(counts))
