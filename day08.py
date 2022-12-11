total = 0
chars = 0
to_add = 0

for line in open('test.in'):
    line = line.rstrip()
    total += len(line)
    i = 1
    while i < len(line) - 1:
        chars += 1
        if line[i] != '\\':
            i += 1
            continue
        if line[i + 1] == 'x':
            i += 4
        else:
            i += 2
    to_add += sum(c == '"' or c == '\\' for c in line) + 2

print(total - chars)
print(to_add)
