ALL = 65535
values = {}
defs = {}

for line in open('test.in'):
    source, dest = line.rstrip().split(' -> ')
    parts = source.split()
    if len(parts) == 1:
        if source.isdigit():
            values[dest] = int(source)
        else:
            defs[dest] = (lambda x: x, source)
    elif len(parts) == 2:
        if parts[0] != 'NOT':
            raise ValueError('unexpected unary operator ' + parts[0])
        if parts[1].isdigit():
            values[dest] = ALL - int(parts[1])
        else:
            defs[dest] = (lambda x: ALL - x, parts[1])
    else:
        if len(parts) != 3:
            raise ValueError('unexpected number of tokens in expression ' + source)
        op1 = int(parts[0]) if parts[0].isdigit() else parts[0]
        op2 = int(parts[2]) if parts[2].isdigit() else parts[2]
        if parts[1] == 'AND':
            defs[dest] = (lambda x, y: x & y, op1, op2)
        elif parts[1] == 'OR':
            defs[dest] = (lambda x, y: x | y, op1, op2)
        elif parts[1] == 'LSHIFT':
            defs[dest] = (lambda x, y: (x << y) & ALL, op1, op2)
        elif parts[1] == 'RSHIFT':
            defs[dest] = (lambda x, y: x >> y, op1, op2)
        else:
            raise ValueError('unexpected operator ' + parts[1])

def eval_wire(wire):
    if isinstance(wire, int):
        return wire
    if wire.isdigit():
        return int(wire)
    if wire in values:
        return values[wire]
    if len(defs[wire]) == 2:
        res = defs[wire][0](eval_wire(defs[wire][1]))
    else:
        res = defs[wire][0](eval_wire(defs[wire][1]), eval_wire(defs[wire][2]))
    values[wire] = res
    return res

# for c in 'defghixy':
#     print(eval_wire(c))

initial_values = dict(values)
res1 = eval_wire('a')
print(res1)

values = dict(initial_values)
values['b'] = res1
print(eval_wire('a'))
