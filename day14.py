file = open('test.in')

# mem = {}
# mask0 = ~0
# mask1 = 0
# for line in file:
#     op, val = line[:-1].split(' = ')
#     if op == 'mask':
#         mask0 = ~0
#         mask1 = 0
#         for i in range(36):
#             if val[i] == '0':
#                 mask0 &= ~(1 << (35 - i))
#             elif val[i] == '1':
#                 mask1 |= 1 << (35 - i)
#     else:
#         address = int(op[4:-1])
#         val = (int(val) & mask0) | mask1
#         mem[address] = val

# print(sum(kvp[1] for kvp in mem.items()))

mem = {}
mask1 = 0
mask_float = set([(~0, 0)])
for line in file:
    op, val = line[:-1].split(' = ')
    if op == 'mask':
        mask1 = 0
        mask_float = set([(~0, 0)])
        for i in range(36):
            if val[i] == '1':
                mask1 |= 1 << (35 - i)
            elif val[i] == 'X':
                new_mask_float = set()
                m1 = 1 << (35 - i)
                m0 = ~m1
                for e0, e1 in mask_float:
                    new_mask_float.add((e0, e1 | m1))
                    new_mask_float.add((e0 & m0, e1))
                mask_float = new_mask_float
    else:
        address = int(op[4:-1])
        address |= mask1
        for m0, m1 in mask_float:
            mem[(address & m0) | m1] = int(val)

print(sum(kvp[1] for kvp in mem.items()))
