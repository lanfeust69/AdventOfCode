monkeys = {}
for line in open('test.in'):
    name, job = line.rstrip().split(': ')
    if job.isdigit():
        monkeys[name] = int(job)
    else:
        monkeys[name] = tuple(job.split())

part2 = False

def evaluate(monkey):
    if part2 and monkey == 'humn':
        return ((1, 0), (0, 1))
    job = monkeys[monkey]
    if isinstance(job, int):
        return ((0, job), (0, 1))
    (n1, d1), op, (n2, d2) = evaluate(job[0]), job[1], evaluate(job[2])
    if sum(x[0] != 0 for x in [n1, d1, n2, d2]) > 1:
        raise ValueError('too many me !')
    if op == '+':
        numer = (n1[0] * d2[1] + n1[1] * d2[0] + n2[0] * d1[1] + n2[1] * d1[0], n1[1] * d2[1] + n2[1] * d1[1])
        denom = (d1[0] * d2[1] + d1[1] * d2[0], d1[1] * d2[1])
    elif op == '-':
        numer = (n1[0] * d2[1] + n1[1] * d2[0] - n2[0] * d1[1] - n2[1] * d1[0], n1[1] * d2[1] - n2[1] * d1[1])
        denom = (d1[0] * d2[1] + d1[1] * d2[0], d1[1] * d2[1])
    elif op == '*':
        numer = (n1[0] * n2[1] + n1[1] * n2[0], n1[1] * n2[1])
        denom = (d1[0] * d2[1] + d1[1] * d2[0], d1[1] * d2[1])
    else:
        numer = (n1[0] * d2[1] + n1[1] * d2[0], n1[1] * d2[1])
        denom = (d1[0] * n2[1] + d1[1] * n2[0], d1[1] * n2[1])
    return numer, denom

res1 = evaluate('root')
print(res1[0][1] // res1[1][1])

part2 = True
monkeys['root'] = (monkeys['root'][0], '-', monkeys['root'][2])
res2 = evaluate('root')
print(res2)
print(-res2[0][1] // res2[0][0])
