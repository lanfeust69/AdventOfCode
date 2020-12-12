program = [int(n) for n in open('test.in').readline().split(',')]

def run(program):
    ip = 0
    while True:
        if program[ip] == 99:
            break
        elif program[ip] == 1:
            program[program[ip + 3]] = program[program[ip + 1]] + program[program[ip + 2]]
            ip += 4
        elif program[ip] == 2:
            program[program[ip + 3]] = program[program[ip + 1]] * program[program[ip + 2]]
            ip += 4
        else:
            raise ValueError
    return program

for noun in range(100):
    for verb in range(100):
        program[1] = noun
        program[2] = verb
        to_run = program[:]
        run(to_run)
        if to_run[0] == 19690720:
            print(noun * 100 + verb)
            break
