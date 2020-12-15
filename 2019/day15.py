import itertools

program = {i: int(n) for i, n in enumerate(open('test.in').readline().split(','))}
# program = {i: int(n) for i, n in enumerate('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'.split(','))}

cur_input = 1
def next_input(_):
    global cur_input
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

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ip = 0
rel_base = 0
x, y = 0, 0
oxygen = None
grid = {(0, 0): 'X'}
todo = set(dirs)
while len(todo) > 0:
    current = set([(x, y)])
    parents = {}
    visited = set(current)
    move = -1
    while move == -1:
        next = set()
        for p in current:
            for dir in dirs:
                neigh = (p[0] + dir[0], p[1] + dir[1])
                if neigh in visited:
                    continue
                if p != (x, y):
                    parents[neigh] = p
                visited.add(neigh)
                if neigh in todo:
                    dest = neigh
                    while dest in parents:
                        dest = parents[dest]
                    move = dirs.index((dest[0] - x, dest[1] - y))
                    break
                if grid[neigh] == '#':
                    continue
                next.add(neigh)
            if move != -1:
                break
        current = next
    cur_input = move + 1 # 1-based...
    dest = (x + dirs[move][0], y + dirs[move][1])
    halted, outputs, ip, rel_base = run_to_output_or_halt(program, ip, rel_base)
    res = outputs[0]
    if dest in todo:
        todo.remove(dest)
    if res == 0:
        grid[dest] = '#'
    else:
        x, y = dest
        for dir in dirs:
            neigh = (x + dir[0], y + dir[1])
            if neigh not in grid:
                todo.add(neigh)
        if res == 1:
            grid[dest] = '.'
        else:
            grid[dest] = 'D'
            oxygen = dest

minx, maxx, miny, maxy = min(p[0] for p in grid), max(p[0] for p in grid), min(p[1] for p in grid), max(p[1] for p in grid)
for y in reversed(range(miny, maxy + 1)):
    line = ''
    for x in range(minx, maxx + 1):
        line += grid.get((x, y), ' ')
    print(line)

current = set([(0, 0)])
visited = set(current)
distance = 0
found = False
while not found:
    distance += 1
    next = set()
    for p in current:
        for dir in dirs:
            neigh = (p[0] + dir[0], p[1] + dir[1])
            if neigh in visited or grid[neigh] == '#':
                continue
            visited.add(neigh)
            if grid[neigh] == 'D':
                found = True
                break 
            next.add(neigh)
    current = next

print(distance)

current = set([oxygen])
visited = set(current)
distance = -1
while len(current) > 0:
    distance += 1
    next = set()
    for p in current:
        for dir in dirs:
            neigh = (p[0] + dir[0], p[1] + dir[1])
            if neigh in visited or grid[neigh] == '#':
                continue
            visited.add(neigh)
            next.add(neigh)
    current = next

print(distance)
