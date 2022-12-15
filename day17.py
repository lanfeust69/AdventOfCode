rocks = [
    (4, [15]),
    (3, [2, 7, 2]),
    (3, [7, 4, 4]), # first line is the bottom one
    (1, [1, 1, 1, 1]),
    (2, [3, 3]),
]
for line in open('test.in'):
    pattern = line.rstrip()
# pattern = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
field = [0]
wind = 0
first_empty = 0

def display(nb_lines):
    if nb_lines == 0:
        nb_lines = len(field)
    for i in range(len(field) - 1, len(field) - nb_lines - 1, -1):
        print(''.join('#' if field[i] & (1 << j) else '.' for j in range(7)))
    print()

def add_rock(rock):
    width, shape = rocks[rock % len(rocks)]
    global wind, first_empty
    r, c = first_empty + 3, 2
    while r + len(shape) >= len(field):
        field.append(0)
    while True:
        # wind
        dc = 1 if pattern[wind] == '>' else -1
        wind = (wind + 1) % len(pattern)
        if 0 <= c + dc <= 7 - width:
            ok = True
            for i in range(len(shape)):
                if field[r + i] & (shape[i] << (c + dc)) != 0:
                    ok = False
                    break
            if ok:
                c += dc
        # fall
        if r == 0:
            break
        ok = True
        for i in range(len(shape)):
            if field[r - 1 + i] & (shape[i] << c) != 0:
                ok = False
                break
        if ok:
            r -= 1
        else:
            break
    for i in range(len(shape)):
        field[r + i] |= shape[i] << c
        if field[r + i] != 0:
            first_empty = max(first_empty, r + i + 1)

nb_block = 0
all_states = {}
before_cycle = -1
cycle_at = -1
first_empty_at_cycle = -1

while True:
    add_rock(nb_block)
    field_state = 0
    for k in range(min(first_empty, 26)):
        field_state |= field[first_empty - 1 - k] << (k * 7)
    state = (field_state, nb_block % len(pattern), nb_block % len(rocks))
    if state in all_states:
        print('found cycle from', all_states[state], 'to', nb_block)
        before_cycle = all_states[state]
        cycle_at = nb_block
        first_empty_at_cycle = first_empty
        break
    else:
        all_states[state] = nb_block
    nb_block += 1
    if nb_block % 1000000 == 0:
        print(nb_block)

# found cycle from 203 to 17407178
# found cycle from 213 to 17407188 -> first_empty = 27336864

len_cycle = cycle_at - before_cycle
todo = (1000000000000 - before_cycle) % len_cycle
field = [0]
wind = 0
first_empty = 0

for nb_block in range(before_cycle + todo):
    if nb_block % 1000000 == 0:
        print(nb_block, '/', before_cycle + todo)
    add_rock(nb_block)
    if nb_block == before_cycle:
        first_empty_before_cycle = first_empty

cycle_height = first_empty_at_cycle - first_empty_before_cycle

print(first_empty + cycle_height * ((1000000000000 - before_cycle) // len_cycle))
