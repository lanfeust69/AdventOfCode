for line in open('test.in'):
    path = line.rstrip().split(',')

dirs = {'se': (1, 0), 'nw': (-1, 0), 'ne': (0, 1), 'sw': (0, -1), 'n': (-1, 1), 's': (1, -1)}
x, y = 0, 0
further = 0
for d in path:
    x, y = x + dirs[d][0], y + dirs[d][1]
    further = max(further, max(abs(x), abs(y), abs(x + y)))

print(max(abs(x), abs(y), abs(x + y)))
print(further)
