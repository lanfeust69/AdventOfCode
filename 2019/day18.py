import heapq

file = open('test.in')

grid = [l[:-1] for l in file]
height = len(grid)
width = len(grid[0])
pos = {}
starts = []

for r in range(height):
    for c in range(width):
        if grid[r][c] in ['@', '&', '*', '%']:
            starts.append(grid[r][c])
            pos[grid[r][c]] = (r, c)
        if 'a' <= grid[r][c] <= 'z':
            pos[grid[r][c]] = (r, c)

nb_keys = len(pos) - len(starts) # starting points '@', '&', '*' and '%' are not keys

def grid_neighbors(p):
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        r, c = p[0] + dr, p[1] + dc
        if r >= 0 and r < height and c >= 0 and c < width and grid[r][c] != '#':
            yield r, c

def find_neighbors(node):
    neighbors = {}
    syms, keys = node
    for robot in range(len(syms)):
        r, c = pos[syms[robot]]
        todo = set([(r, c)])
        visited = set([(r, c)])
        d = 0
        while len(todo) > 0:
            d += 1
            next_todo = set()
            for p in todo:
                for rr, cc in grid_neighbors(p):
                    if (rr, cc) in visited:
                        continue
                    visited.add((rr, cc))
                    ch = grid[rr][cc]
                    if 'a' <= ch <= 'z' and ch not in keys:
                        new_keys = keys.union([ch])
                        new_syms = tuple(list(syms[:robot]) + [ch] + list(syms[robot + 1:]))
                        neighbors[(new_syms, new_keys)] = d
                        continue
                    if 'A' <= ch <= 'Z' and ch.lower() not in keys:
                        continue
                    next_todo.add((rr, cc))
            todo = next_todo
    return neighbors

start = tuple(starts), frozenset()

todo = set(start)
done = set()
distances = {start: 0}
heap = []
heapq.heappush(heap, (0, start))
cur_print = 1000
while len(heap) > 0:
    dist, node = heapq.heappop(heap)
    if node in done:
        continue
    if len(node[1]) == nb_keys:
        print(dist)
        break
    done.add(node)
    for neighbor, d in find_neighbors(node).items():
        if neighbor in done:
            continue
        if neighbor not in distances or dist + d < distances[neighbor]:
            distances[neighbor] = dist + d
            heapq.heappush(heap, (dist + d, neighbor))
    if len(distances) >= cur_print:
        print('nb distances :', len(distances))
        cur_print += 1000
