from functools import cache

wires = {}
gates = {}

for line in open('test.in'):
    line = line.rstrip()
    if ':' in line:
        wire, val = line.split(': ')
        wires[wire] = int(val)
    elif '->' in line:
        parts = line.split()
        gates[parts[-1]] = (parts[1], parts[0], parts[2])

def solve(wire):
    if wire in wires:
        return wires[wire]
    op, op1, op2 = gates[wire]
    op1, op2 = solve(op1), solve(op2)
    if op == 'AND':
        res = op1 & op2
    elif op == 'OR':
        res = op1 | op2
    else:
        res = op1 ^ op2
    wires[wire] = res
    return res

zs = [w for w in wires if w[0] == 'z'] + [w for w in gates if w[0] == 'z']
zs.sort()
zs.reverse()

res = 0
for z in zs:
    res = (res << 1) | solve(z)

print(res)

def find_op(op, op1, op2):
    for wire, gate in gates.items():
        if gate == (op, op1, op2) or gate == (op, op2, op1):
            return wire
    return None

carries = []
swaps = []
for i in range(45):
    x, y, z = f'x{i:02}', f'y{i:02}', f'z{i:02}'
    op_xor = ''
    op_and = ''
    z_opes = None
    z_ok = True
    for wire, gate in gates.items():
        if wire == z:
            if gate[0] != 'XOR':
                z_ok = False
            z_opes = (gate[1], gate[2])
        if gate[1] in (x, y):
            if gate[2] not in (x, y):
                raise ValueError(f'problem with {gate}')
            if gate[0] == 'XOR':
                op_xor = wire
            elif gate[0] == 'AND':
                op_and = wire
            else:
                raise ValueError(f'problem with {gate}')
    if not z_ok:
        # look for expected ope
        if i == 0:
            expected = (x, y)
        else:
            expected = (carries[-1], op_xor)
        correct_wire = find_op('XOR', expected[0], expected[1])
        if not correct_wire:
            raise ValueError(f'problem with {z}: cannot find expected gate')
        swaps.append((z, correct_wire))
        gates[z], gates[correct_wire] = gates[correct_wire], gates[z]
        z_opes = (gates[z][1], gates[z][2])
        if op_and == z:
            op_and = correct_wire

    if not z_opes or op_xor == '' or op_and == '':
        raise ValueError(f'problem with {i}: missing part')
    else:
        if i == 0:
            if op_xor != z:
                correct_wire = find_op('XOR', x, y)
                if not correct_wire:
                    raise ValueError(f'problem with {z}: cannot find expected gate')
                swaps.append((z, correct_wire))
                gates[z], gates[correct_wire] = gates[correct_wire], gates[z]
            carries.append(op_and)
        else:
            prev_carry = carries[-1]
            if z_opes != (op_xor, prev_carry) and z_opes != (prev_carry, op_xor):
                correct_wire = find_op('XOR', op_xor, prev_carry)
                if correct_wire:
                    swaps.append((z, correct_wire))
                    gates[z], gates[correct_wire] = gates[correct_wire], gates[z]
                    z_opes = (op_xor, prev_carry)
                elif op_xor in z_opes:
                    real_carry = z_opes[0] if z_opes[1] == op_xor else z_opes[1]
                    carries.pop()
                    carries.append(real_carry)
                    swaps.append((prev_carry, real_carry))
                    gates[prev_carry], gates[real_carry] = gates[real_carry], gates[prev_carry]
                    if op_and == real_carry:
                        op_and = prev_carry
                    prev_carry = real_carry
                elif prev_carry in z_opes:
                    real_xor = z_opes[0] if z_opes[1] == prev_carry else z_opes[1]
                    swaps.append((op_xor, real_xor))
                    gates[op_xor], gates[real_xor] = gates[real_xor], gates[op_xor]
                    if op_and == real_xor:
                        op_and = op_xor
                    op_xor = real_xor
                else:
                    raise ValueError(f'problem with {z}: two possibilities')
            tmp_carry = find_op('AND', prev_carry, op_xor)
            if not tmp_carry:
                raise ValueError(f'problem with {i} tmp_carry not found')
            carry = find_op('OR', tmp_carry, op_and)
            if not carry:
                for wire, gate in gates.items():
                    if gate[0] == 'OR' and (gate[1] == op_and or gate[2] == op_and):
                        # op_and seems OK
                        real_tmp_carry = gate[1] if gate[2] == op_and else gate[2]
                        swaps.append((tmp_carry, real_tmp_carry))
                        gates[tmp_carry], gates[real_tmp_carry] = gates[real_tmp_carry], gates[tmp_carry]
                        carry = wire
                        break
                    if gate[0] == 'OR' and (gate[1] == tmp_carry or gate[2] == tmp_carry):
                        # tmp_carry seems OK
                        real_and = gate[1] if gate[2] == tmp_carry else gate[2]
                        swaps.append((op_and, real_and))
                        gates[op_and], gates[real_and] = gates[real_and], gates[op_and]
                        carry = wire
                        break
                else:
                    raise ValueError(f'problem with {i} carry not found')
            carries.append(carry)

for a, b in swaps:
    print(f'{a} <=> {b}')

print(','.join(sorted(wire for swap in swaps for wire in swap)))
