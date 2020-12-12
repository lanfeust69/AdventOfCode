program = [int(n) for n in open('test.in').readline().split(',')]

instructions = {
    1: (2, True, lambda v: v[0] + v[1], lambda ip, _: ip + 4),
    2: (2, True, lambda v: v[0] * v[1], lambda ip, _: ip + 4),
    3: (0, True, lambda _: 5, lambda ip, _: ip + 2),
    4: (1, False, lambda _: 0, lambda ip, _: ip + 2),
    5: (2, False, lambda _: 0, lambda ip, v: ip + 3 if v[0] == 0 else v[1]),
    6: (2, False, lambda _: 0, lambda ip, v: ip + 3 if v[0] != 0 else v[1]),
    7: (2, True, lambda v: 1 if v[0] < v[1] else 0, lambda ip, _: ip + 4),
    8: (2, True, lambda v: 1 if v[0] == v[1] else 0, lambda ip, _: ip + 4)
}

def run(program):
    ip = 0
    outputs = []
    while True:
        if program[ip] == 99:
            break
        opcode = program[ip] % 100
        nb_in, has_out, op, ip_move = instructions[opcode]
        modes = program[ip] // 100
        vals = []
        for i in range(nb_in):
            vals.append(program[program[ip + 1 + i]] if (modes // 10**i) % 10 == 0 else program[ip + 1 + i])
        if has_out:
            res = op(vals)
            program[program[ip + nb_in + 1]] = res
        elif opcode == 4:
            outputs.append(vals[0])
        ip = ip_move(ip, vals)
    return outputs

outputs = run(program)
print(outputs)
print(outputs[-1])
