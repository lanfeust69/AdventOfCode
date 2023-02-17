ops = {}
def make_f(base_op, is_imm_a, is_imm_b):
    def f(regs, a, b, c):
        operand1 = a if is_imm_a else regs[a]
        operand2 = b if is_imm_b else regs[b]
        regs[c] = base_op(operand1, operand2)
        return regs
    return f
for name, base_op in [('add', lambda a, b: a + b), ('mul', lambda a, b: a * b), ('ban', lambda a, b: a & b), ('bor', lambda a, b: a | b)]:
    for imm in [True, False]:
        ops[name + ('i' if imm else 'r')] = make_f(base_op, False, imm)
for imm in [True, False]:
    ops['seti' if imm else 'setr'] = make_f(lambda a, _: a, imm, True)
for name, base_op in [('gt', lambda a, b: 1 if a > b else 0), ('eq', lambda a, b: 1 if a == b else 0)]:
    for imms in [(True, False), (False, True), (False, False)]:
        ops[name + ('i' if imms[0] else 'r') + ('i' if imms[1] else 'r')] = make_f(base_op, *imms)

program = []
ip_reg = 0
for line in open('test.in'):
    if line[0] == '#':
        ip_reg = int(line[4])
        continue
    tokens = line.rstrip().split()
    program.append((tokens[0], tuple(map(int, tokens[1:]))))

a, b, c = 0, 0, 0
seen = set()
prev = 0
nb = 0
while True:
    nb += 1
    if nb % 10000000 == 0:
        print(nb)
    a = c | 65536
    c = 521363
    b = a & 255
    while True:
        c = ((c + b) * 65899) & 16777215
        # print(a, b, c)
        if a < 256:
            break
        b = a // 256
        a = b
        b = a & 255
    # print('=>', c)
    if c in seen:
        print(prev)
        break
    seen.add(c)
    prev = c

exit(0)

regs = [0] * 6
# regs[0] = 1024276
ip = 0
step = 0
while 0 <= ip < len(program):
    if ip == 28:
        print(ip, program[ip], regs)
    step += 1
    if step % 10000000 == 0:
        # print(step)
        break
    op, args = program[ip]
    regs[ip_reg] = ip
    ops[op](regs, *args)
    # print(ip, program[ip], regs)
    ip = regs[ip_reg]
    ip += 1

print('stopped at step', step, 'regs[0] = ', regs[0])
