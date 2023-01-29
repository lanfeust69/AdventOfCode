from collections import deque

program = [line.rstrip().split() for line in open('test.in')]

regs = [{'p': 0}, {'p': 1}]

def val(s, i):
    if s.isdigit() or s[0] == '-':
        return int(s)
    if s in regs[i]:
        return regs[i][s]
    regs[i][s] = 0
    return 0

eips = [0, 0]
queues = [deque(), deque()]
snd1 = 0

def step(p):
    eip = eips[p]
    if eip < 0 or eip >= len(program):
        return False
    inst, *ops = program[eip]
    if inst == 'jgz' and val(ops[0], p) > 0:
        eip += val(ops[1], p)
    else:
        eip += 1
    if inst == 'set':
        regs[p][ops[0]] = val(ops[1], p)
    elif inst == 'add':
        regs[p][ops[0]] = val(ops[0], p) + val(ops[1], p)
    elif inst == 'mul':
        regs[p][ops[0]] = val(ops[0], p) * val(ops[1], p)
    elif inst == 'mod':
        regs[p][ops[0]] = val(ops[0], p) % val(ops[1], p)
    elif inst == 'snd':
        queues[1 - p].append(val(ops[0], p))
        if p == 1:
            global snd1
            snd1 += 1
    elif inst == 'rcv':
        if len(queues[p]) == 0:
            return False
        regs[p][ops[0]] = queues[p].popleft()
    eips[p] = eip
    return True

run0, run1 = True, True
while run0 or run1:
    run0 = step(0)
    run1 = step(1)

print(snd1) # 7366 is too high
