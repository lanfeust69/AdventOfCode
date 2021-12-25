bits = []
for line in open('test.in'):
    for d in line[:-1]:
        digit = int(d, 16)
        for i in range(4):
            bits.append(0 if (digit & (1 << (3 - i))) == 0 else 1)

def int_val(pos, length):
    val = 0
    for _ in range(length):
        val = val * 2 + bits[pos]
        pos += 1
    return val

def varint_val(pos):
    val = 0
    while True:
        last = bits[pos] == 0
        pos += 1
        for _ in range(4):
            val = val * 2 + bits[pos]
            pos += 1
        if last:
            break
    return pos, val

s = 0

def parse(pos):
    global s
    version = int_val(pos, 3)
    s += version
    type_id = int_val(pos + 3, 3)
    pos += 6
    if type_id == 4:
        return varint_val(pos)
    else:
        vals = []
        is_length = bits[pos] == 0
        pos += 1
        if is_length:
            length = int_val(pos, 15)
            pos += 15
            end = pos + length
            while pos < end:
                pos, val = parse(pos)
                vals.append(val)
        else:
            nb = int_val(pos, 11)
            pos += 11
            for _ in range(nb):
                pos, val = parse(pos)
                vals.append(val)
        if type_id == 0:
            res = sum(vals)
        elif type_id == 1:
            res = 1
            for v in vals:
                res *= v
        elif type_id == 2:
            res = min(vals)
        elif type_id == 3:
            res = max(vals)
        elif type_id == 5:
            res = 1 if vals[0] > vals[1] else 0
        elif type_id == 6:
            res = 1 if vals[0] < vals[1] else 0
        elif type_id == 7:
            res = 1 if vals[0] == vals[1] else 0
        return pos, res

_, res = parse(0)
print(res)
