program = [line.rstrip().split() for line in open('test.in')]

regs = {}

def val(s):
    if s.isdigit() or s[0] == '-':
        return int(s)
    if s in regs:
        return regs[s]
    regs[s] = 0
    return 0

def step(eip):
    if eip < 0 or eip >= len(program):
        return eip
    inst, *ops = program[eip]
    if inst == 'jnz' and val(ops[0]) != 0:
        eip += val(ops[1])
    else:
        eip += 1
    if inst == 'set':
        regs[ops[0]] = val(ops[1])
    elif inst == 'sub':
        regs[ops[0]] = val(ops[0]) - val(ops[1])
    elif inst == 'mul':
        regs[ops[0]] = val(ops[0]) * val(ops[1])
        global res
        res += 1
    return eip

eip = 0
res = 0

while 0 <= eip < len(program):
    eip = step(eip)

print(res)

# counts number of composites between b and c, step 17
b = 100000 + 84 * 100
c = b + 17000
primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
    101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353]
h = 0
for n in range(b, c + 1, 17):
    for p in primes:
        if n % p == 0:
            h += 1
            break

print(h)
