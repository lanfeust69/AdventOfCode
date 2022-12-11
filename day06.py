grid1 = [[False] * 1000 for _ in range(1000)]
grid2 = [[False] * 1000 for _ in range(1000)]

parser1 = {'turn on ': lambda cur: True, 'turn off ': lambda cur: False, 'toggle ': lambda cur: not cur }
parser2 = {'turn on ': lambda cur: cur + 1, 'turn off ': lambda cur: max(0, cur - 1), 'toggle ': lambda cur: cur + 2 }
for line in open('test.in'):
    for s in parser1:
        if line.startswith(s):
            f1 = parser1[s]
            f2 = parser2[s]
            skip = len(s)
    c1, c2 = line.rstrip()[skip:].split(' through ')
    x1, y1 = map(int, c1.split(','))
    x2, y2 = map(int, c2.split(','))
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid1[x][y] = f1(grid1[x][y])
            grid2[x][y] = f2(grid2[x][y])

nb_lit = sum(sum(row) for row in grid1)
brightness = sum(sum(row) for row in grid2)

print(nb_lit, brightness)
