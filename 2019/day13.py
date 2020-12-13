import itertools

program = {i: int(n) for i, n in enumerate(open('test.in').readline().split(','))}

# inputs = []
# cur_input = -1
# def next_input(_):
#     global cur_input
#     cur_input += 1
#     return inputs[cur_input]

cur_input = 0
def next_input(_):
    return cur_input

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

def display(board, data):
    changed = {(data[i * 3], data[i * 3 + 1]): data[i * 3 + 2] for i in range(len(data) // 3)}
    board.update(changed)
    minx, maxx, miny, maxy = min(p[0] for p in board), max(p[0] for p in board), min(p[1] for p in board), max(p[1] for p in board)
    for y in range(miny, maxy + 1):
        line = ''
        for x in range(minx, maxx + 1):
            val = board.get((x, y))
            if val == 0:
                line += ' '
            elif val == 1:
                line += 'X'
            elif val == 2:
                line += '#'
            elif val == 3:
                line += '+'
            elif val == 4:
                line += 'o'
            else:
                line += '?'
        print(line)
    return board

# print(len(set((board[i * 3], board[i * 3 + 1]) for i in range(len(board) // 3) if board[i * 3 + 2] == 2)))

program[0] = 2
inputs = [0]
ip = 0
rel_base = 0
all_out = []
board = {}
score = 0
first = True
paddle = 0
ball = 0
while True:
    halted, outputs, ip, rel_base = run_to_output_or_halt(program, ip, rel_base)
    if halted:
        break
    all_out += outputs
    if len(all_out) % 3 != 0:
        continue
    if len(all_out) > 2 and all_out[-3] == -1 and all_out[-2] == 0:
        score = all_out[-1]
        if first:
            display(board, all_out[:-3])
            print('score is', score)
        all_out.clear()
        first = False
        continue
    if all_out[-1] == 3:
        paddle = all_out[-3]
    if all_out[-1] == 4:
        ball = all_out[-3]
        if not first:
            if ball < paddle:
                cur_input = -1
            elif ball > paddle:
                cur_input = 1
            else:
                cur_input = 0
    # if not first and all_out[-1] != 0:
    #     display(board, all_out)
    #     print('score is', score)

print('score is', score)
