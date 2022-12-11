clues = {
    'children': lambda x: x == 3,
    'cats': lambda x: x == 7,
    'samoyeds': lambda x: x == 2,
    'pomeranians': lambda x: x == 3,
    'akitas': lambda x: x == 0,
    'vizslas': lambda x: x == 0,
    'goldfish': lambda x: x == 5,
    'trees': lambda x: x == 3,
    'cars': lambda x: x == 2,
    'perfumes': lambda x: x == 1
}
clues['cats'] = lambda x: x > 7
clues['pomeranians'] = lambda x: x < 3
clues['goldfish'] = lambda x: x < 5
clues['trees'] = lambda x: x > 3

for line in open('test.in'):
    pos = line.index(':')
    facts = line[pos + 2:]
    ok = True
    for fact in facts.split(', '):
        category, nb = fact.split(': ')
        if not clues[category](int(nb)):
            ok = False
            break
    if ok:
        print(line[:pos].split()[1])
