import itertools

program = {i: int(n) for i, n in enumerate(open('test.in').readline().split(','))}

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

ip = 0
rel_base = 0
commands = [
    'west', 'west', 'take loom', 'east', 'east', 'north', 'north', 'take mutex',
    'east', 'take tambourine', 'west', 'south', 'west', 'take antenna', 'south',
    'take hologram', 'south', 'take mug', 'north', 'west', 'take astronaut ice cream',
    'east', 'north', 'north', 'north', 'north', 'take space heater', 'north', 'east'
]
items = ['mutex', 'loom', 'tambourine', 'hologram', 'space heater', 'antenna', 'astronaut ice cream', 'mug']
for item in items:
    commands.append('drop ' + item)
for i in range(1 << len(items)):
    for j in range(len(items)):
        if (1 << j) & i:
            commands.append('take ' + items[j])
    commands.append('east')
    for j in range(len(items)):
        if (1 << j) & i:
            commands.append('drop ' + items[j])

cur_command = 0
halted = False
found = False
while not halted:
    o = ''
    while not o.endswith('Command?\n'):
        halted, outputs, ip, rel_base = run_to_output_or_halt(program, ip, rel_base)
        if halted:
            break
        o += chr(outputs[0])
    if not found and cur_command > 35 and commands[cur_command - 1] == 'east' and o.find('Security Checkpoint') == -1:
        found = True
        print(o)
        inputs += [ord(c) for c in 'inv'] + [10]
        continue
    if not found and cur_command < len(commands):
        inputs += [ord(c) for c in commands[cur_command]] + [10]
        cur_command += 1
        continue
    print(o)
    new_command = input()
    inputs += [ord(c) for c in new_command] + [10]
