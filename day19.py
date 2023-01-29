diagram = [line for line in open('test.in')]

r, c = 0, diagram[0].index('|')
dr, dc = 1, 0
letters = ''
nb_steps = 0

while True:
    nb_steps += 1
    r, c = r + dr, c + dc
    if diagram[r][c] == ' ':
        break
    if diagram[r][c] != '+':
        if diagram[r][c] not in '-|':
            letters += diagram[r][c]
        continue
    for drr, dcc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if drr == -dr and dcc == -dc:
            continue
        if diagram[r + drr][c + dcc] != ' ':
            dr, dc = drr, dcc
            break

print(letters)
print(nb_steps)
