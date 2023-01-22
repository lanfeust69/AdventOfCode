regs = {}

def val(s):
    if s[0].isdigit() or s[0] == '-':
        return int(s)
    if s in regs:
        return regs[s]
    regs[s] = 0
    return 0

highest = -1000000
for line in open('test.in'):
    tokens = line.rstrip().split()
    op1, op2 = val(tokens[-3]), val(tokens[-1])
    op = tokens[-2]
    cnd = False
    if op == '<':
        cnd = op1 < op2
    elif op == '<=':
        cnd = op1 <= op2
    elif op == '>':
        cnd = op1 > op2
    elif op == '>=':
        cnd = op1 >= op2
    elif op == '==':
        cnd = op1 == op2
    elif op == '!=':
        cnd = op1 != op2
    if not cnd:
        continue
    initial = val(tokens[0])
    delta = val(tokens[2])
    if tokens[1] == 'dec':
        delta = -delta
    regs[tokens[0]] = initial + delta
    highest = max(highest, initial + delta)

print(max(regs[x] for x in regs))
print(highest)
