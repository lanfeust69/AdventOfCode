pwd = [c for c in 'abcdefgh']

instructions = [line.rstrip().split() for line in open('test.in')]
revert = False

rev_rot_based = [0] * len(pwd)
for i in range(len(pwd)):
    dest = (i * 2 + 1 + (i >= 4)) % len(pwd)
    rev_rot_based[dest] = (dest - i) % len(pwd)

seq = [''.join(pwd)]

def process(tokens, pwd):
    if tokens[0] == 'swap':
        if tokens[1] == 'position':
            a, b = int(tokens[2]), int(tokens[-1])
        else:
            a, b = pwd.index(tokens[2]), pwd.index(tokens[-1])
        pwd[a], pwd[b] = pwd[b], pwd[a]
    elif tokens[0] == 'rotate':
        if tokens[1] == 'based':
            pos = pwd.index(tokens[-1])
            if revert:
                rot = rev_rot_based[pos]
            else:
                rot = len(pwd) - (pos + 1 + (pos >= 4))
        elif (tokens[1] == 'right' and not revert) or (tokens[1] == 'left' and revert):
            rot = len(pwd) - int(tokens[-2])
        else:
            rot = int(tokens[-2])
        pwd = pwd[rot:] + pwd[:rot]
    elif tokens[0] == 'reverse':
        a, b = int(tokens[2]), int(tokens[-1])
        pwd = pwd[:a] + list(reversed(pwd[a:b + 1])) + pwd[b + 1:]
    elif tokens[0] == 'move':
        a, b = int(tokens[2]), int(tokens[-1])
        if revert:
            a, b = b, a
        if a < b:
            pwd = pwd[:a] + pwd[a + 1:b + 1] + [pwd[a]] + pwd[b + 1:]
        else:
            pwd = pwd[:b] + [pwd[a]] + pwd[b:a] + pwd[a + 1:]
    else:
        raise ValueError('unexpected token ' + tokens[0])
    seq.append(''.join(pwd))
    return pwd

for tokens in instructions:
    pwd = process(tokens, pwd)

print(''.join(pwd))

pwd = [c for c in 'fbgdceah']
revert = True
i = 0
seq.reverse()
for tokens in reversed(instructions):
    pwd = process(tokens, pwd)
    # i += 1
    # if ''.join(pwd) != seq[i]:
    #     raise ValueError('bug !!')

print(''.join(pwd))
