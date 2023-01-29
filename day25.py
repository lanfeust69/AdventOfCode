state = ''
cur_input, cur_val = '', -1
cur = [[0, 0, ''], [0, 0, '']]
states = {}
target = -1

for line in open('test.in'):
    line = line.strip()
    if line.startswith('Begin'):
        state = line[-2]
    elif line.startswith('Perform'):
        target = int(line.split()[-2])
    elif len(line) == 0:
        if cur_input:
            states[cur_input] = tuple(tuple(cur[i]) for i in range(2))
    elif line.startswith('In state'):
        cur_input = line[-2]
    elif line.startswith('If'):
        cur_val = int(line[-2])
    elif line.startswith('- Write'):
        cur[cur_val][0] = int(line[-2])
    elif line.startswith('- Move'):
        cur[cur_val][1] = 1 if 'right' in line else -1
    elif line.startswith('- Continue'):
        cur[cur_val][2] = line[-2]

print(state, target, states)

positive = [0]
negative = []
def get_val(pos):
    if pos >= 0:
        while pos >= len(positive):
            positive.append(0)
        return positive[pos]
    pos = -pos - 1
    while pos >= len(negative):
        negative.append(0)
    return negative[pos]

def set_val(pos, val):
    if pos >= 0:
        while pos >= len(positive):
            positive.append(0)
        positive[pos] = val
        return
    pos = -pos - 1
    while pos >= len(negative):
        negative.append(0)
    negative[pos] = val

pos = 0
for step in range(target):
    if step % 1000000 == 0:
        print('step', step)
    write, move, state = states[state][get_val(pos)]
    set_val(pos, write)
    pos += move

print(sum(positive) + sum(negative))
