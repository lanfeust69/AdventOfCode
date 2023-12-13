lines = [line.rstrip() for line in open('test.in')]
values = set()
new_values = set(map(int, lines[0][7:].split()))
for line in lines[2:]:
    if line == '':
        continue
    if 'map' in line:
        new_values |= values
        values, new_values = new_values, set()
        continue
    dest, source, count = map(int, line.split())
    found = set()
    for v in values:
        if source <= v < source + count:
            found.add(v)
            new_values.add(dest + v - source)
    values -= found

new_values |= values
print(min(*new_values))

values = set()
seed_counts = list(map(int, lines[0][7:].split()))
new_values = set((seed_counts[i * 2], seed_counts[i * 2 + 1]) for i in range(len(seed_counts) // 2))
for line in lines[2:]:
    if line == '':
        continue
    if 'map' in line:
        new_values |= values
        values, new_values = new_values, set()
        continue
    dest, source, count = map(int, line.split())
    to_remove = set()
    to_add = set()
    for v, c in values:
        if v + c <= source or v >= source + count:
            continue
        to_remove.add((v, c))
        if v < source:
            to_add.add((v, source - v))
        start = max(v, source)
        nb = min(v + c - start, source + count - start)
        new_values.add((start + dest - source, nb))
        if start + nb < v + c:
            to_add.add((start + nb, v + c - (start + nb)))
    values = (values - to_remove) | to_add

new_values |= values
print(len(new_values), 'intervals')
print(min(v[0] for v in new_values))
