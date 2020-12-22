import itertools

program = {i: int(n) for i, n in enumerate(open('test.in').readline().split(','))}
# program = {i: int(n) for i, n in enumerate('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'.split(','))}

cur_input = -1
inputs = []
def next_input(_):
    global cur_input
    cur_input += 1
    return inputs[cur_input]

instructions = {
    1: (2, True, lambda v: v[0] + v[1], lambda ip, _: ip + 4),
    2: (2, True, lambda v: v[0] * v[1], lambda ip, _: ip + 4),
    3: (0, True, next_input, lambda ip, _: ip + 2),
    4: (1, False, lambda _: 0, lambda ip, _: ip + 2),
    5: (2, False, lambda _: 0, lambda ip, v: ip + 3 if v[0] == 0 else v[1]),
    6: (2, False, lambda _: 0, lambda ip, v: ip + 3 if v[0] != 0 else v[1]),
    7: (2, True, lambda v: 1 if v[0] < v[1] else 0, lambda ip, _: ip + 4),
    8: (2, True, lambda v: 1 if v[0] == v[1] else 0, lambda ip, _: ip + 4),
    9: (1, False, lambda _: 0, lambda ip, _: ip + 2)
}

def run_to_output_or_halt(program, start_ip, rel_base):
    ip = start_ip
    outputs = []
    while True:
        if program[ip] == 99:
            return True, outputs, ip, rel_base
        opcode = program[ip] % 100
        nb_in, has_out, op, ip_move = instructions[opcode]
        modes = program[ip] // 100
        vals = []
        for i in range(nb_in):
            mode = (modes // 10**i) % 10
            if mode == 0:
                vals.append(program.get(program[ip + 1 + i], 0))
            elif mode == 1:
                vals.append(program[ip + 1 + i])
            elif mode == 2:
                vals.append(program.get(program[ip + 1 + i] + rel_base, 0))
            else:
                assert(False)
        if has_out:
            res = op(vals)
            mode = (modes // 10**nb_in) % 10
            if mode == 0:
                program[program[ip + nb_in + 1]] = res
            elif mode == 2:
                program[program[ip + nb_in + 1] + rel_base] = res
            else:
                assert(False)
        elif opcode == 9:
            rel_base += vals[0]
        elif opcode == 4:
            outputs.append(vals[0])
            ip = ip_move(ip, vals)
            return False, outputs, ip, rel_base
        ip = ip_move(ip, vals)

def run(program):
    halted = False
    ip = 0
    rel_base = 0
    res = []
    while not halted:
        halted, outputs, ip, rel_base = run_to_output_or_halt(program, ip, rel_base)
        res += outputs
    return res

def is_in_beam(x, y):
    global cur_input, inputs
    cur_input = -1
    inputs = [x, y]
    _, outputs, _, _ = run_to_output_or_halt(dict(program), 0, 0)
    return outputs[0] == 1

widths = {49: (31, 36)}
x = 50
inf, sup = 31, 36
while True:
    while not is_in_beam(x, inf):
        inf += 1
    while is_in_beam(x, sup + 1):
        sup += 1
    widths[x] = inf, sup
    if sup - inf + 1 >= 100 and x >= 149:
        top = x - 99
        top_inf, top_sup = widths[top]
        if top_sup - inf >= 99:
            print(top * 10000 + top_sup - 99)
            break
    x += 1
