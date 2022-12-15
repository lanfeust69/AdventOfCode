sensors = []
beacons = set()
for line in open('test.in'):
    words = line.rstrip().split()
    x, y = int(words[2][2:-1]), int(words[3][2:-1])
    xb, yb = int(words[-2][2:-1]), int(words[-1][2:])
    sensors.append((x, y, abs(xb - x) + abs(yb - y)))
    beacons.add((xb, yb))

def possible(row, inf, sup):
    row_beacons = sorted(x for x, y in beacons if y == row)
    intervals = []
    for x, y, d in sensors:
        if abs(row - y) > d:
            continue
        intervals.append((x - d + abs(row - y), x + d - abs(row - y)))

    intervals.sort()
    res = []
    cur_end = inf - 1
    for start, end in intervals:
        start = min(start, sup + 1)
        if start > cur_end + 1:
            s = cur_end + 1
            while s in row_beacons:
                s += 1
            for xb in row_beacons:
                if s < xb <= start:
                    res.append((s, xb - 1))
                    s = xb + 1
                    while s in row_beacons:
                        s += 1
            if s < start:
                res.append((s, start - 1))
        cur_end = max(cur_end, end)
        if cur_end >= sup:
            break
    if cur_end < sup:
        s = cur_end + 1
        while s in row_beacons:
            s += 1
        for xb in row_beacons:
            if s < xb <= sup + 1:
                res.append((s, xb - 1))
                s = xb + 1
                while s in row_beacons:
                    s += 1
        if s <= sup:
            res.append((s, sup))
    return res

def solve1(row):
    inf, sup = -1000000000, 1000000000
    res = sup - inf + 1 - sum(e - s + 1 for s, e in possible(row, inf, sup))
    for x in (x for x, y in beacons if y == row):
        if inf <= x <= sup:
            res -= 1
    return res

print(solve1(2000000))

inf, sup = 0, 4000000
found = False
for row in range(sup + 1):
    for interval in possible(row, inf, sup):
        if len(interval) > 0:
            found = True
            print(row, interval[0], row + interval[0] * sup)
            break
    if found:
        break
