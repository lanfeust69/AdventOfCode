beacons = []
scanners = []
for line in open('test.in'):
    if len(line) < 2:
        continue
    if 'scanner' in line:
        if len(beacons) > 0:
            scanners.append(beacons)
        beacons = []
    else:
        beacons.append(tuple(map(int, line.split(','))))
scanners.append(beacons)

def try_match_coord(c1, c2):
    if abs(c1[0]) == abs(c1[1]) or abs(c1[0]) == abs(c1[2]) or abs(c1[1]) == abs(c1[2]):
        # print('ambiguity in', c1)
        return None
    mapping = []
    signs = []
    for i in range(3):
        found = False
        for j in range(3):
            if abs(c2[j]) == abs(c1[i]):
                found = True
                mapping.append(j)
                signs.append(1 if c2[j] == c1[i] else -1)
                break
        if not found:
            return None
    return tuple(mapping), tuple(signs)    

def rotate(c, rotation):
    mapping, signs = rotation
    return tuple(c[mapping[i]] * signs[i] for i in range(3))

def translate(c, translation):
    return tuple(c[i] + translation[i] for i in range(3))

def try_match(s1, s2):
    for i in range(len(s1)):
        coords  = [tuple(s1[j][k] - s1[i][k] for k in range(3)) for j in range(i + 1, len(s1))]
        for j in range(len(s2)):
            matchings = {}
            for k in range(len(s2)):
                if k == j:
                    continue
                coord = tuple(s2[k][l] - s2[j][l] for l in range(3))
                for c in range(len(coords)):
                    m = try_match_coord(coords[c], coord)
                    if m is None:
                        continue
                    if m not in matchings:
                        matchings[m] = [(i, j)]
                    matchings[m].append((c + i + 1, k))
            for m, l in matchings.items():
                if len(l) < 12:
                    continue
                # found !
                rotated_j = rotate(s2[j], m)
                translation = tuple(s1[i][k] - rotated_j[k] for k in range(3))
                return translation, m
    return None

def transform(scanner, t):
    translation, rotation = t
    return [translate(rotate(c, rotation), translation) for c in scanner]

known = [False] * len(scanners)
known[0] = True
done = [False] * len(scanners)
positions = [None] * len(scanners)
positions[0] = (0, 0, 0)
while sum(known) < len(scanners):
    for i in range(len(scanners)):
        if done[i]:
            continue
        if not known[i]:
            continue
        done[i] = True
        for j in range(len(scanners)):
            if known[j]:
                continue
            m = try_match(scanners[i], scanners[j])
            if m:
                known[j] = True
                positions[j] = m[0]
                scanners[j] = transform(scanners[j], m)
    print(sum(known), 'known')

print(len(set(beacon for scanner in scanners for beacon in scanner)))
max_d = 0
for i in range(len(scanners) - 1):
    for j in range(i + 1, len(scanners)):
        d = sum(abs(positions[j][k] - positions[i][k]) for k in range(3))
        max_d = max(max_d, d)
print(max_d)
