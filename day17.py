import heapq

grid = [[int(c) for c in line.rstrip()] for line in open('test.in')]
h, w = len(grid), len(grid[0])
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve(is_part2):
    heap = []
    heapq.heappush(heap, (0, (0, 0, 0, 0)))
    heapq.heappush(heap, (0, (0, 0, 1, 0)))
    dists = {(0, 0, 0, 0): 0, (0, 0, 1, 0): 0}

    while len(heap):
        dist, (r, c, d, nb) = heapq.heappop(heap)
        if (r, c, d, nb) in dists and dists[(r, c, d, nb)] < dist:
            continue
        if is_part2 and nb < 4:
            rr, cc = r + dirs[d][0], c + dirs[d][1]
            new_dist = dist + grid[rr][cc]
            neigh = (rr, cc, d, nb + 1)
            if neigh not in dists or new_dist < dists[neigh]:
                dists[neigh] = new_dist
                heapq.heappush(heap, (new_dist, neigh))
            continue
        if (r, c) == (h - 1, w - 1):
            print(dist)
            break
        for dd in range(-1, 2):
            rr, cc = r + dirs[(d + dd) % 4][0], c + dirs[(d + dd) % 4][1]
            if not (0 <= rr < h and 0 <= cc < w):
                continue
            new_dist = dist + grid[rr][cc]
            if dd == 0:
                if (not is_part2 and nb == 3) or (is_part2 and nb == 10):
                    continue
                neigh = (rr, cc, d, nb + 1)
                if neigh not in dists or new_dist < dists[neigh]:
                    dists[neigh] = new_dist
                    heapq.heappush(heap, (new_dist, neigh))
            else:
                if is_part2:
                    min_r, min_c = r + dirs[(d + dd) % 4][0] * 4, c + dirs[(d + dd) % 4][1] * 4
                    if not (0 <= min_r < h and 0 <= min_c < w):
                        continue
                neigh = (rr, cc, (d + dd) % 4, 1)
                if neigh not in dists or new_dist < dists[neigh]:
                    dists[neigh] = new_dist
                    heapq.heappush(heap, (new_dist, neigh))

solve(False)
solve(True)
