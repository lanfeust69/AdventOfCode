import itertools

program = [int(n) for n in open('test.in').readline().split(',')]
# program = [int(n) for n in '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'.split(',')]

inputs = [0, 0]
cur_input = -1
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
    8: (2, True, lambda v: 1 if v[0] == v[1] else 0, lambda ip, _: ip + 4)
}

def run_to_output_or_halt(program, start_ip):
    ip = start_ip
    outputs = []
    while True:
        if program[ip] == 99:
            return True, outputs, ip
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
            return False, outputs, ip
        ip = ip_move(ip, vals)

def run(program):
    halted = False
    ip = 0
    res = []
    while not halted:
        halted, outputs, ip = run_to_output_or_halt(program, ip)
        res += outputs
    return res

best = 0
for perm in itertools.permutations(range(5, 10)):
    to_run = [program[:] for _ in range(5)]
    cur_inputs = [-1] * 5
    all_inputs = [[setting] for setting in perm]
    all_inputs[0].append(0)
    ips = [0] * 5
    running = 0
    thrust = 0
    halted = [False] * 5
    while not halted[running]:
        cur_input = cur_inputs[running]
        inputs = all_inputs[running]
        halted[running], outputs, ips[running] = run_to_output_or_halt(to_run[running], ips[running])
        cur_inputs[running] = cur_input
        running = (running + 1) % 5
        if len(outputs) > 0:
            thrust = outputs[-1]
            all_inputs[running].append(thrust)
    best = max(best, thrust)

print(best)
