total = 0
prev0 = 1000000
prev1 = 1000000
prev2 = 1000000
for line in open('test.in'):
    depth = int(line)
    if depth > prev2:
        total += 1
    (prev2, prev1, prev0) = (prev1, prev0, depth)

print(total)
