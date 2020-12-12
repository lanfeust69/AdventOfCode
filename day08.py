import sys
sys.stdin = open('test.in')

program = [(l.split()[0], int(l.split()[1])) for l in sys.stdin.readlines()]

def run(program):
    acc, ip = 0, 0
    seen = set()
    while True:
        if ip in seen:
            return False, acc
        if ip >= len(program):
            return True, acc
        seen.add(ip)
        ins, p = program[ip]
        if ins == 'acc':
            acc += p
            ip += 1
        elif ins == 'jmp':
            ip += p
        else:
            ip += 1

for i in range(len(program)):
    if program[i][0] == 'acc':
        continue
    ins = program[i][0]
    patched = 'jmp' if ins == 'nop' else 'nop'
    program[i] = (patched, program[i][1])
    terminate, acc = run(program)
    if terminate:
        print(acc)
    program[i] = (ins, program[i][1])

# print(run(program)[1])
