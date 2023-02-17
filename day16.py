ops = []
def make_f(base_op, is_imm_a, is_imm_b):
    def f(regs, a, b, c):
        operand1 = a if is_imm_a else regs[a]
        operand2 = b if is_imm_b else regs[b]
        regs[c] = base_op(operand1, operand2)
        return regs
    return f
for name, base_op in [('add', lambda a, b: a + b), ('mul', lambda a, b: a * b), ('ban', lambda a, b: a & b), ('bor', lambda a, b: a | b)]:
    for imm in [True, False]:
        ops.append((name + ('i' if imm else 'r'), make_f(base_op, False, imm)))
for imm in [True, False]:
    ops.append(('seti' if imm else 'setr', make_f(lambda a, _: a, imm, True)))
for name, base_op in [('gt', lambda a, b: 1 if a > b else 0), ('eq', lambda a, b: 1 if a == b else 0)]:
    for imms in [(True, False), (False, True), (False, False)]:
        ops.append((name + ('i' if imms[0] else 'r') + ('i' if imms[1] else 'r'), make_f(base_op, *imms)))

nb_op_codes = len(ops)
program = []
regs_in = [0] * 4
op_code = [0] * 4
res = 0
nb_blank = 0
candidates = [set(range(nb_op_codes)) for _ in range(nb_op_codes)]
for line in open('test.in'):
    line = line.rstrip()
    if not len(line):
        nb_blank += 1
        continue
    if nb_blank == 3:
        program.append(list(map(int, line.split())))
        continue
    nb_blank = 0
    if line.startswith('Before'):
        regs_in = list(map(int, line[9:-1].split(', ')))
    elif line.startswith('After'):
        regs_out = list(map(int, line[9:-1].split(', ')))
        nb_compatible = 0
        for i in range(nb_op_codes):
            name, op = ops[i]
            if op(regs_in[:], *op_code[1:]) == regs_out:
                nb_compatible += 1
                # print(f"[{', '.join(map(str, regs_in))}] -> {name}({' '.join(map(str, op_code[1:]))}) -> [{', '.join(map(str, regs_out))}]")
            else:
                candidates[op_code[0]].discard(i)
        if nb_compatible >= 3:
            res += 1
    else:
        op_code = list(map(int, line.split()))

print(res)

assignment = [-1] * nb_op_codes
progress = True
while progress:
    progress = False
    for code, possibilities in enumerate(candidates):
        if assignment[code] != -1:
            continue
        if len(possibilities) > 1:
            continue
        progress = True
        v = possibilities.pop()
        assignment[code] = v
        for s in candidates:
            s.discard(v)

if any(a == -1 for a in assignment):
    raise ValueError('could not definitely assign op_codes')

regs = [0] * 4
for op_code, a, b, c in program:
    regs = ops[assignment[op_code]][1](regs, a, b, c)

print(regs[0])
