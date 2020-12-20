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

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
inputs = [ord(c) for c in 'A,B,B,A,C,A,A,C,B,C\nR,8,L,12,R,8\nR,12,L,8,R,10\nR,8,L,8,L,8,R,8,R,10\nn\n']
outputs = run(program)
to_print = ''
for c in outputs:
    to_print += chr(c)
print(to_print)
print(outputs[-1])
grid = [l for l in to_print.split('\n')[:33] if len(l) > 0]
height = len(grid)
width = len(grid[0])
path = 'R'
r, c = next((r, c) for r in range(height) for c in range(width) if grid[r][c] == '^')
cur_dir = 0
while True:
    move = 0
    rr, cc = r + dirs[cur_dir][0], c + dirs[cur_dir][1]
    while rr >= 0 and rr < height and cc >= 0 and cc < width and grid[rr][cc] == '#':
        move += 1
        r, c = rr, cc
        rr, cc = r + dirs[cur_dir][0], c + dirs[cur_dir][1]
    path += ',' + str(move)
    cur_dir = (cur_dir + 1) % 4
    rr, cc = r + dirs[cur_dir][0], c + dirs[cur_dir][1]
    if rr >= 0 and rr < height and cc >= 0 and cc < width and grid[rr][cc] == '#':
        path += ',R'
        continue
    cur_dir = (cur_dir + 2) % 4
    rr, cc = r + dirs[cur_dir][0], c + dirs[cur_dir][1]
    if rr >= 0 and rr < height and cc >= 0 and cc < width and grid[rr][cc] == '#':
        path += ',L'
        continue
    # end of path
    break

print(path)
# path = R,8,L,12,R,8,R,12,L,8,R,10,R,12,L,8,R,10,R,8,L,12,R,8,R,8,L,8,L,8,R,8,R,10,R,8,L,12,R,8,R,8,L,12,R,8,R,8,L,8,L,8,R,8,R,10,R,12,L,8,R,10,R,8,L,8,L,8,R,8,R,10
# path = A,B,B,A,C,A,A,C,B,C
# A = R,8,L,12,R,8
# B = R,12,L,8,R,10
# C = R,8,L,8,L,8,R,8,R,10

res = 0
for row in range(1, height - 1):
    for col in range(1, width - 1):
        if grid[row][col] != '.' and all(grid[row - dr][col + dc] == '#' for dr, dc in dirs):
            res += row * col
print(res)
