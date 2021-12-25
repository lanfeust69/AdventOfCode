program = [line[:-1] for line in open('test.in')]
register_ids = {chr(119 + r): r for r in range(4)}
operations = {
    'add': lambda a, b: a + b,
    'mul': lambda a, b: a * b,
    'div': lambda a, b: a // b,
    'mod': lambda a, b: a % b,
    'eql': lambda a, b: 1 if a == b else 0
}

def run(inputs):
    registers = [0] * 4
    input_pos = 0
    v1, v2, v3 = 0, 0, 0
    for i in range(len(program)):
        line = program[i]
        inst = line.split()
        if inst[0] == 'inp':
            registers[register_ids[inst[1]]] = inputs[input_pos]
            input_pos += 1
            start = registers[:]
        else:
            a = register_ids[inst[1]]
            b = registers[register_ids[inst[2]]] if inst[2] in register_ids else int(inst[2])
            if i % 18 == 4:
                v1 = b
            elif i % 18 == 5:
                v2 = b
            elif i % 18 == 15:
                v3 = b
            registers[a] = operations[inst[0]](registers[a], b)
        if i % 18 == 17:
            w, x, y, z = start
            print('start', start, 'z % 26 =', z % 26, v1, v2, v3)
            # print(registers)
            # eq = 1 if w != z % 26 + v2 else 0
            # print([w, eq, (w + v3) * eq, (z // v1 * 25 + w + v3) * eq + z // v1])
    return registers

# registers = run([int(c) for c in '97919997299495'])
registers = run([int(c) for c in '51619131181131'])
print(registers)
