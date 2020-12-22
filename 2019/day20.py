maze = [l[:-1] for l in open('test.in')]
height = len(maze)
width = len(maze[0])

def maze_neighbors(p):
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        r, c = p[0] + dr, p[1] + dc
        if r >= 0 and r < height and c >= 0 and c < width and maze[r][c] != '#':
            yield r, c

labels = {}
labels_pos = {}

for row in range(height):
    for col in range(width):
        if maze[row][col] != '.':
            continue
        for r, c in maze_neighbors((row, col)):
            letter = maze[r][c]
            if 'A' <= letter <= 'Z':
                other_letter = maze[row + (r - row) * 2][col + (c - col) * 2]
                label = letter + other_letter if r > row or c > col else other_letter + letter
                inner = (r > row and row < height // 2) or (r < row and row > height // 2)
                inner = inner or (c > col and c < width // 2) or (c < col and c > width // 2)
                delta = 1 if inner else -1
                labels[(row, col)] = label, delta
                labels_pos[(label, delta)] = (row, col)

graph = {}

for row in range(height):
    for col in range(width):
        if maze[row][col] != '.':
            continue
        neighbors = []
        for r, c in maze_neighbors((row, col)):
            if maze[r][c] == '.':
                neighbors.append(((r, c), 0))
        if (row, col) in labels:
            label, delta = labels[(row, col)]
            if label != 'AA' and label != 'ZZ':
                other = labels_pos[(label, -delta)]
                neighbors.append((other, delta))
        graph[(row, col)] = neighbors

start = labels_pos[('AA', -1)], 0
finish = labels_pos[('ZZ', -1)], 0
todo = set([start])
visited = set(todo)
d = 0
done = False
parents = {}
while len(todo) > 0 and not done:
    d += 1
    next_todo = set()
    for p, depth in todo:
        for n, delta in graph[p]:
            n_depth = depth + delta
            if n_depth < 0:
                continue
            if (n, n_depth) in visited:
                continue
            parents[(n, n_depth)] = p, depth
            if (n, n_depth) == finish:
                done = True
                print(d)
                break
            visited.add((n, n_depth))
            next_todo.add((n, n_depth))
    todo = next_todo

# cur = finish
# while cur in parents:
#     if cur[0] in labels:
#         print(cur, labels[cur[0]][0])
#     else:
#         print(cur)
#     cur = parents[cur]
