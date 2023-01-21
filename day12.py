program = [line.rstrip().split() for line in open('test.in')]

def val(s):
    if s in regs:
        return regs[s]
    return int(s)

for c_val in range(2):
    eip = 0
    regs = {'a': 0, 'b': 0, 'c': c_val, 'd': 0}

    while eip < len(program):
        inst = program[eip]
        if inst[0] == 'jnz' and val(inst[1]):
            eip += int(inst[2])
        else:
            eip += 1
        if inst[0] == 'cpy':
            regs[inst[2]] = val(inst[1])
        elif inst[0] == 'inc':
            regs[inst[1]] += 1
        elif inst[0] == 'dec':
            regs[inst[1]] -= 1

    print(regs['a'])
