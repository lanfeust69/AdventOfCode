track = [line.rstrip() for line in open('test.in')]

h, w = len(track), len(track[0])

def find_start():
    for r in range(h):
        for c in range(w):
            if track[r][c] == 'S':
                return r, c

r0, c0 = find_start()

times = [[-1] * w for _ in range(h)]
r, c, t = r0, c0, 0
times[r0][c0] = 0
while track[r][c] != 'E':
    t += 1
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        rr, cc = r + dr, c + dc
        if track[rr][cc] != '#' and times[rr][cc] == -1:
            times[rr][cc] = t
            r, c = rr, cc
            break

res1, res2 = 0, 0
for r in range(h):
    for c in range(w):
        if times[r][c] == -1:
            continue
        t0 = times[r][c]
        for dr in range(-20, 21):
            max_dc = 20 - abs(dr)
            for dc in range(-max_dc, max_dc + 1):
                t = abs(dr) + abs(dc)
                rr, cc = r + dr, c + dc
                if not (0 <= rr < h and 0 <= cc < w):
                    continue
                if times[rr][cc] >= times[r][c] + t + 100:
                    res2 += 1
                    if t == 2:
                        res1 += 1

print(res1)
print(res2)
