import math

modules = {}
states = {}
conjs = set()
broadcast = []

conj = ''

for line in open('test.in'):
    line = line.rstrip()
    name, dests = line.split(' -> ')
    dests = dests.split(', ')
    if name[0] == '%':
        modules[name[1:]] = ('%', dests)
        states[name[1:]] = False
        if 'rx' in dests:
            raise ValueError('rx is supposed to be activated by a single conjunction')
    elif name[0] == '&':
        modules[name[1:]] = ('&', dests)
        states[name[1:]] = {}
        conjs.add(name[1:])
        if 'rx' in dests:
            if conj:
                raise ValueError('rx is supposed to be activated by a single conjunction')
            conj = name[1:]
    else:
        broadcast = dests

for name, module in modules.items():
    for dest in module[1]:
        if dest in conjs:
            states[dest][name] = False

nb_push = 0

if not conj:
    raise ValueError('rx is supposed to be activated by a single conjunction')
nb_input = len(states[conj])
input_periods = {}

def push():
    global nb_push
    nb_push += 1
    counts = [1, 0] # 1 for the initial low from the button
    pulses = [(d, False, 'broadcaster') for d in broadcast]
    pos = 0
    while pos < len(pulses):
        module, level, source = pulses[pos]
        counts[level] += 1
        if module not in modules:
            pos += 1
            continue
        t, dests = modules[module]
        if t == '%' and not level:
            states[module] = not states[module]
            for dest in dests:
                pulses.append((dest, states[module], module))
        elif t == '&':
            states[module][source] = level
            sent = any(not states[module][s] for s in states[module])
            if sent and conj in dests and module not in input_periods:
                input_periods[module] = nb_push
            for dest in dests:
                pulses.append((dest, sent, module))
        pos += 1
    return counts

low, high = 0, 0
for _ in range(1000):
    new_pulses = push()
    low += new_pulses[0]
    high += new_pulses[1]

print(low * high)

while len(input_periods) != nb_input:
    push()

print(math.lcm(*input_periods.values()))
