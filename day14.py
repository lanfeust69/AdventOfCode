def parse(s):
    p, v = s.split(' v=')
    return tuple(map(int, p[2:].split(','))), tuple(map(int, v.split(',')))

robots = [parse(line.rstrip()) for line in open('test.in')]

h, w = 103, 101
t = 100

res = [0] * 4
for (x, y), (dx, dy) in robots:
    xx = ((x + t * dx) % w + w) % w
    yy = ((y + t * dy) % h + h) % h
    if xx == w // 2 or yy == h // 2:
        continue
    res[(xx < w // 2) * 2 + (yy < h // 2)] += 1

print(res[0] * res[1] * res[2] * res[3])

def count_long_lines(grid, is_row):
    nb_long = 0
    end_of_line = w if is_row else h
    def at(i, j):
        return grid[i][j] if is_row else grid[j][i]
    for line in range(h if is_row else w):
        pos = 0
        while pos < end_of_line and at(line, pos) == ' ':
            pos += 1
        start = pos
        longest = 1
        while pos < end_of_line:
            if at(line, pos) == '#':
                longest = max(longest, pos - start + 1)
            else:
                while pos < end_of_line and at(line, pos) == ' ':
                    pos += 1
                start = pos
            pos += 1
        if longest > 20:
            nb_long += 1
    return nb_long

pos = [robot[0] for robot in robots]
for t in range(h * w):
    if t > 0 and t % 500 == 0:
        print(t)
    grid = [[' '] * w for _ in range(h)]
    for i in range(len(pos)):
        x, y = pos[i]
        grid[y][x] = '#'
        pos[i] = (x + robots[i][1][0] + w) % w, (y + robots[i][1][1] + h) % h

    nb_long_rows = count_long_lines(grid, True)
    nb_long_cols = count_long_lines(grid, False)

    if nb_long_rows >= 2 and nb_long_cols >= 2:
        print('>>>', t)
        for row in grid:
            print(''.join(row))
    t += 1
