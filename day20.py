ranges = [tuple(map(int, line.rstrip().split('-'))) for line in open('test.in')]
ranges.sort()
ranges.append((2**32 - 1, 2**32))

cur = 0
nb_allowed = 0
first_allowed = -1
for start, end in ranges:
    if start > cur:
        if first_allowed == -1:
            first_allowed = cur
        nb_allowed += start - cur
    cur = max(cur, end + 1)

print(first_allowed)
print(nb_allowed)
