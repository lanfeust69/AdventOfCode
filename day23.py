registers = {'a': 1, 'b': 0}
program = [line.rstrip() for line in open('test.in')]

eip = 0
while eip < len(program):
    line = program[eip]
    inst = line[:3]
    offset = 1
    if inst == 'hlf':
        registers[line[-1]] //= 2
    elif inst == 'tpl':
        registers[line[-1]] *= 3
    elif inst == 'inc':
        registers[line[-1]] += 1
    elif inst == 'jmp':
        offset = int(line[4:])
    elif (inst == 'jie' and registers[line[4]] % 2 == 0) or (inst == 'jio' and registers[line[4]] == 1):
        offset = int(line[7:])
    eip += offset

print(registers['b'])
