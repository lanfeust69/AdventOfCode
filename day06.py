import functools

lines_raw = [line.rstrip('\r\n') for line in open('test.in')]
nb_lines = len(lines_raw) - 1
ops = lines_raw[-1].split()
nb_cols = len(ops)
bounds = [i for i in range(len(lines_raw[-1])) if lines_raw[-1][i] != ' '] + [100000]
lines = [[lines_raw[i][bounds[j]:bounds[j + 1] - 1] for j in range(nb_cols)] for i in range(nb_lines)]
opes = {'*': lambda a, b: a * b, '+': lambda a, b: a + b}

res1, res2 = 0, 0
for i in range(nb_cols):
    op = opes[ops[i]]
    block = [lines[j][i] for j in range(nb_lines)]
    res1 += functools.reduce(op, map(int, block))
    transposed = [''.join(block[j][i] for j in range(nb_lines)) for i in range(len(block[0]))]
    res2 += functools.reduce(op, map(int, transposed))

print(res1)
print(res2)
