cur = 0
cals = []
for line in open('test.in'):
    line = line.rstrip()
    if line:
        cur += int(line)
    else:
        cals.append(cur)
        cur = 0

cals.append(cur)
cals.sort()

print(cals[-3:])
print(sum(cals[-3:]))
