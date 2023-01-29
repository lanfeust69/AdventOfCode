for line in open('test.in'):
    dance = line.rstrip().split(',')

def perform(s):
    p = [c for c in s]
    for move in dance:
        if move[0] == 's':
            n = int(move[1:])
            p = p[-n:] + p[:-n]
        elif move[0] == 'x':
            a, b = map(int, move[1:].split('/'))
            p[a], p[b] = p[b], p[a]
        else:
            a, b = move[1:].split('/')
            a, b = p.index(a), p.index(b)
            p[a], p[b] = p[b], p[a]
    return ''.join(p)

start = ''.join(chr(97 + i) for i in range(16))
print(perform(start))

step = 0
seen = {}
seen[start] = 0
current = start
nb = 1000000000
while nb > 0:
    step += 1
    current = perform(current)
    if current in seen:
        if nb > step:
            nb = nb % (step - seen[current])
    else:
        seen[current] = step
    nb -= 1

print(current)
