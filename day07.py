grid = [line.rstrip('\r\n') for line in open('test.in')]
n = len(grid[0])
nb_time_lines = [0] * n
nb_time_lines[grid[0].index('S')] = 1
res1 = 0
for i in range(1, len(grid)):
    next_line = [0] * n
    for j in range(n):
        x = nb_time_lines[j]
        if x:
            if grid[i][j] == '^':
                res1 += 1
                next_line[j - 1] += x
                next_line[j + 1] += x
            else:
                next_line[j] += x
    nb_time_lines = next_line

print(res1)
print(sum(nb_time_lines))
