import itertools

program = {i: int(n) for i, n in enumerate(open('test.in').readline().split(','))}

cur_input = -1
inputs = []
def next_input(_):
    global cur_input
    if cur_input >= len(inputs) - 1:
        return -1
    else:
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

def run_to_drain_or_halt(program, start_ip, rel_base):
    ip = start_ip
    outputs = []
    nb_no_input = 0
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
                assert False
        if has_out:
            res = op(vals)
            mode = (modes // 10**nb_in) % 10
            if mode == 0:
                program[program[ip + nb_in + 1]] = res
            elif mode == 2:
                program[program[ip + nb_in + 1] + rel_base] = res
            else:
                assert False
            if opcode == 3 and res == -1:
                nb_no_input += 1
                if nb_no_input >= 2:
                    ip = ip_move(ip, vals)
                    return False, outputs, ip, rel_base
        elif opcode == 9:
            rel_base += vals[0]
        elif opcode == 4:
            outputs.append(vals[0])
            nb_no_input = 0
        ip = ip_move(ip, vals)

programs = [[dict(program), 0, 0, [i], -1] for i in range(50)]
drained = [False] * 50
nat_x, nat_y = 0, 0
prev_nat_sent_y = None
while True:
    if all(drained):
        if nat_y == prev_nat_sent_y:
            print(nat_y)
            break
        programs[0][3] += [nat_x, nat_y]
        prev_nat_sent_y = nat_y
    for p in range(50):
        code, ip, rel_base, inputs, cur_input = programs[p]
        halted, outputs, ip, rel_base = run_to_drain_or_halt(code, ip, rel_base)
        drained[p] = True
        for i in range(len(outputs) // 3):
            dest = outputs[i * 3]
            x = outputs[i * 3 + 1]
            y = outputs[i * 3 + 2]
            if dest == 255:
                nat_x, nat_y = x, y
            else:
                programs[dest][3] += [x, y]
                drained[dest] = False
        programs[p][1] = ip
        programs[p][2] = rel_base
        programs[p][4] = cur_input
