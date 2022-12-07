chars = []
badges = []
group = []
i = 0

for line in open('test.in'):
    line = line.rstrip()
    l1, l2 = line[:len(line) // 2], line[len(line) // 2:]
    for c in l1:
        if c in l2:
            chars.append(c)
            break
    group.append(line)
    i += 1
    if i % 3 == 0:
        for c in group[0]:
            if c in group[1] and c in group[2]:
                badges.append(c)
                break
        group.clear()

print(sum(ord(c) - 96 if c >= 'a' else ord(c) - 38 for c in chars))
print(sum(ord(c) - 96 if c >= 'a' else ord(c) - 38 for c in badges))
