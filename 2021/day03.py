ls = []
for line in open('test.in'):
    ls.append(line[:-1]) # strip eol

v = [0, 0]
for crit in [True, False]:
    lines = ls[:]
    pos = 0
    while len(lines) > 1:
        n = sum(1 for line in lines if line[pos] == '1')
        most_common = 1 if n >= len(lines) / 2 else 0
        target = str(most_common if crit else 1 - most_common)
        lines = [line for line in lines if line[pos] == target]
        pos += 1
    v[crit] = int(lines[0], 2)

print(v[0] * v[1])
