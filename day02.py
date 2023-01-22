infs, sups = 0, 0
divs = 0

for line in open('test.in'):
    row = list(map(int, line.rstrip().split()))
    infs += min(row)
    sups += max(row)
    found = False
    for i in range(len(row) - 1):
        for j in range(i + 1, len(row)):
            a, b = max(row[i], row[j]), min(row[i], row[j])
            if a % b == 0:
                found = True
                divs += a // b
                break
        if found:
            break

print(sups - infs)
print(divs)
