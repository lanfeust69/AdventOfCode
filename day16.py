grid = [line.rstrip() for line in open('test.in')]
h, w = len(grid), len(grid[0])
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve(r0, c0, d0):
    beams = set([(r0, c0, d0)])
    grid_beams = [[set() for _ in range(w)] for _ in range(h)]
    while len(beams):
        new_beams = set()
        for r, c, d in beams:
            rr, cc, dd = r + dirs[d][0], c + dirs[d][1], d
            if rr < 0 or rr >= h or cc < 0 or cc >= w:
                continue
            if d % 2 == 0 and grid[rr][cc] == '|':
                if (rr, cc, 1) not in grid_beams[rr][cc]:
                    grid_beams[rr][cc].add((rr, cc, 1))
                    new_beams.add((rr, cc, 1))
                dd = 3
            elif d % 2 == 1 and grid[rr][cc] == '-':
                if (rr, cc, 0) not in grid_beams[rr][cc]:
                    grid_beams[rr][cc].add((rr, cc, 0))
                    new_beams.add((rr, cc, 0))
                dd = 2
            elif grid[rr][cc] == '/':
                dd = (d + (3 if d % 2 == 0 else 1)) % 4
            elif grid[rr][cc] == '\\':
                dd = (d + (1 if d % 2 == 0 else 3)) % 4
            if (rr, cc, dd) not in grid_beams[rr][cc]:
                grid_beams[rr][cc].add((rr, cc, dd))
                new_beams.add((rr, cc, dd))
        beams = new_beams

    res = 0
    for r in range(h):
        for c in range(w):
            if len(grid_beams[r][c]):
                res += 1
    return res

print(solve(0, -1, 0))

best = 0
for r0 in range(h):
    best = max(best, solve(r0, -1, 0))
    best = max(best, solve(r0, w, 2))
for c0 in range(w):
    best = max(best, solve(-1, c0, 1))
    best = max(best, solve(h, c0, 3))

print(best)
