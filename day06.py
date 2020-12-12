import sys
sys.stdin = open('test.in')

total = 0
current = set()
first = True
for line in sys.stdin:
    if line == '\n':
        total += len(current)
        current = set()
        first = True
        continue
    line = line[:-1]
    if first:
        current = set(line)
        first = False
    else:
        current.intersection_update(line)

total += len(current)

print(total)
