def knot_h(s):
    lens = [ord(c) for c in s] + [17, 31, 73, 47, 23]
    cur = list(range(256))
    skip = 0
    pos = 0
    for _ in range(64):
        for l in lens:
            to_reverse = cur[:l]
            to_reverse.reverse()
            cur = to_reverse + cur[l:]
            shift = (l + skip) % len(cur)
            pos = (pos + shift) % len(cur)
            cur = cur[shift:] + cur[:shift]
            skip += 1

    # 0 should be at pos instead
    cur = cur[-pos:] + cur[:-pos]
    h = []
    for i in range(16):
        x = 0
        for j in range(i * 16, (i + 1) * 16):
            x ^= cur[j]
        h.append(x)
    return h

def display(h):
    s = ''
    for x in h:
        d = hex(x)[2:]
        if len(d) < 2:
            d = '0' + d
        s += d
    return s

total = 0
grid = [[False] * 128 for _ in range(128)]
for i in range(128):
    h = knot_h('stpzcrnm-' + str(i))
    for j in range(16):
        x = h[j]
        pos = 0
        while x > 0:
            if x & 1:
                total += 1
                grid[i][(j + 1) * 8 - 1 - pos] = True
            x >>= 1
            pos += 1

seen = [[False] * 128 for _ in range(128)]
nb_components = 0
for r in range(128):
    for c in range(128):
        if seen[r][c] or not grid[r][c]:
            continue
        nb_components += 1
        seen[r][c] = True
        todo = [(r, c)]
        while len(todo) > 0:
            next_todo = []
            for rr, cc in todo:
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    rrr, ccc = rr + dr, cc + dc
                    if rrr < 0 or rrr >= 128 or ccc < 0 or ccc >= 128 or seen[rrr][ccc] or not grid[rrr][ccc]:
                        continue
                    seen[rrr][ccc] = True
                    next_todo.append((rrr, ccc))
            todo = next_todo

print(total)
print(nb_components)
