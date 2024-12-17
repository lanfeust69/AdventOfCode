lines = [line.rstrip() for line in open('test.in')]
registers = [int(lines[i][12:]) for i in range(3)]
program = list(map(int, lines[-1][9:].split(',')))

def combo(i):
    if i < 4:
        return i
    else:
        return registers[i - 4]

ip = 0
outs = []
while ip < len(program):
    opcode = program[ip]
    operand = program[ip + 1]

    if opcode == 0:
        registers[0] >>= combo(operand)
    elif opcode == 1:
        registers[1] ^= operand
    elif opcode == 2:
        registers[1] = combo(operand) & 7
    elif opcode == 3:
        if registers[0]:
            ip = operand - 2
    elif opcode == 4:
        registers[1] ^= registers[2]
    elif opcode == 5:
        outs.append(combo(operand) & 7)
    elif opcode == 6:
        registers[1] = registers[0] >> combo(operand)
    elif opcode == 7:
        registers[2] = registers[0] >> combo(operand)
    ip += 2

print(','.join(str(out) for out in outs))

# B = A & 7
# B ^= 3
# C = A >> B
# B ^= C
# B ^= 3
# A >>= 3
# out B & 7
# goto 0

def solve(pos, cur_a):
    if pos == -1:
        return cur_a
    for i in range(8):
        if pos == len(program) - 1 and i == 0:
            continue
        a = (cur_a << 3) | i
        b = (i ^ (a >> (i ^ 3))) & 7
        if b != program[pos]:
            continue
        res = solve(pos - 1, a)
        if res:
            return res
    return None

print(solve(len(program) - 1, 0))
