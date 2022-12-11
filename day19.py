transform = {}

start = ''
for line in open('test.in'):
    parts = line.rstrip().split(' => ')
    if len(parts) != 2:
        start = parts[0]
    else:
        if parts[0] in transform:
            transform[parts[0]].append(parts[1])
        else:
            transform[parts[0]] = [parts[1]]

def all_replacements(start):
    for i in range(len(start)):
        if start[i] in transform:
            for repl in transform[start[i]]:
                yield start[:i] + repl + start[i + 1:]
        if i < len(start) - 1 and start[i:i + 2] in transform:
            for repl in transform[start[i:i + 2]]:
                yield start[:i] + repl + start[i + 2:]

print(len(set(all_replacements(start))))

rev_transform = {}
final = []
for k, v in transform.items():
    if k == 'e':
        final = v
    else:
        for s in v:
            rev_transform[s] = k

candidates = [(start, 0)]
distances = {start: 0}
while len(candidates) > 0:
    candidates.sort(key=lambda p: -len(p[0]))
    s, d = candidates.pop()
    if d > distances[s]:
        continue
    for f, t in rev_transform.items():
        pos = 0
        idx = s.find(f, pos)
        while idx != -1:
            reduced = s[:idx] + t + s[idx + len(f):]
            if reduced in final:
                print(d + 2) # +2 for the e->reduced step
                exit(0)
            if reduced not in distances or d + 1 < distances[reduced]:
                candidates.append((reduced, d + 1))
                distances[reduced] = d + 1
            pos = idx + (2 if idx + 1 < len(s) and s[idx + 1].islower() else 1)
            idx = s.find(f, pos)
