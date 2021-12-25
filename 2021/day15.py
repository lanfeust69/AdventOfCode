import heapq

grid0 = [[int(c) - 1 for c in line[:-1]] for line in open('test.in')]
grid = []
for r in grid0:
    row = r[:]
    for i in range(4):
        row += [(v + 1 + i) % 9 for v in r]
    grid.append(row)
for i in range(4):
    for r in range(len(grid0)):
        grid.append([(v + 1 + i) % 9 for v in grid[r]])

h, w = len(grid), len(grid[0])
for r in range(h):
    for c in range(h):
        grid[r][c] += 1

heap = []
heapq.heappush(heap, (0, (0, 0)))
distances = [[100000] * w for _ in range(h)]
distances[0][0] = 0

def neighbors(p):
    r, c = p
    if r > 0:
        yield (r - 1, c)
    if r < h - 1:
        yield (r + 1, c)
    if c > 0:
        yield (r, c - 1)
    if c < w - 1:
        yield (r, c + 1)

while len(heap) > 0:
    d, closest = heapq.heappop(heap)
    if closest == (h - 1, w - 1):
        print(d)
        break
    if d > distances[closest[0]][closest[1]]:
        continue
    for r, c in neighbors(closest):
        if d + grid[r][c] < distances[r][c]:
            distances[r][c] = d + grid[r][c]
            heapq.heappush(heap, (d + grid[r][c], (r, c)))
