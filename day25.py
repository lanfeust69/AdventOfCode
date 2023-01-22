program = [line.rstrip().split() for line in open('test.in')]

# d = a + 633 * 4
# a = d
# while True:
#     a //= 2
#     yield a % 2
#     if a == 0:
#         a = d
a, i = 1, 0
while a < 633 * 4:
    a = a * 2 + i % 2
    i += 1
print(a - 633 * 4)
exit(0)

def val(s):
    if s in regs:
        return regs[s]
    return int(s)

eip = 0
regs = {'a': 198, 'b': 0, 'c': 0, 'd': 0}
outputs = []

while eip < len(program):
    inst = program[eip]
    if inst[0] == 'jnz' and val(inst[1]):
        eip += val(inst[2])
    else:
        eip += 1
    if inst[0] == 'cpy':
        if inst[2] in regs:
            regs[inst[2]] = val(inst[1])
    elif inst[0] == 'inc':
        regs[inst[1]] += 1
    elif inst[0] == 'dec':
        regs[inst[1]] -= 1
    elif inst[0] == 'tgl':
        target = eip - 1 + val(inst[1]) # eip has already been incremented
        if 0 <= target < len(program):
            if program[target][0] == 'inc':
                program[target][0] = 'dec'
            elif program[target][0] == 'dec' or program[target][0] == 'tgl':
                program[target][0] = 'inc'
            if program[target][0] == 'cpy':
                program[target][0] = 'jnz'
            elif program[target][0] == 'jnz':
                program[target][0] = 'cpy'
    elif inst[0] == 'out':
        outputs.append(val(inst[1]))
