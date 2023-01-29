def transforms(s):
    yield s
    rows = s.split('/')
    n = len(rows)
    yield '/'.join(rows[::-1])
    yield '/'.join(r[::-1] for r in rows)
    yield '/'.join(''.join(rows[j][n - 1 - i] for j in range(n)) for i in range(n))
    yield '/'.join(''.join(rows[n - 1 - j][i] for j in range(n)) for i in range(n))
    yield '/'.join(r[::-1] for r in rows[::-1])
    yield '/'.join(''.join(rows[j][i] for j in range(n)) for i in range(n))
    yield '/'.join(''.join(rows[n - 1 - j][n - 1 - i] for j in range(n)) for i in range(n))

rules = {}
for line in open('test.in'):
    src, dst = line.rstrip().split(' => ')
    for transformed in transforms(src):
        if transformed in rules and rules[transformed] != dst:
            raise ValueError('conflict')
        rules[transformed] = dst

grid = ['.#.', '..#', '###']

def enhance(grid):
    size = len(grid)
    if size % 2 == 0:
        res = [''] * (size // 2 * 3)
        for r in range(size // 2):
            for c in range(size // 2):
                cell = '/'.join(grid[r * 2 + i][c * 2:c * 2 + 2] for i in range(2))
                trans = rules[cell].split('/')
                for i in range(3):
                    res[r * 3 + i] += trans[i]
    else:
        res = [''] * (size // 3 * 4)
        for r in range(size // 3):
            for c in range(size // 3):
                cell = '/'.join(grid[r * 3 + i][c * 3:c * 3 + 3] for i in range(3))
                trans = rules[cell].split('/')
                for i in range(4):
                    res[r * 4 + i] += trans[i]
    return res

for _ in range(18):
    grid = enhance(grid)

print(len(grid))
print(sum(sum(c == '#' for c in row) for row in grid))
