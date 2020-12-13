file = open('test.in')

graph = {}
for line in file:
    source, dest = line[:-1].split(' => ')
    qd, nd = dest.split(' ')
    qd = int(qd)
    s = [(x[1], int(x[0])) for x in (p.split(' ') for p in source.split(', '))]
    graph[nd] = (qd, s)

depths = {'ORE': 0}
def find_depth(elem):
    if elem in depths:
        return depths[elem]
    depth = max(find_depth(e[0]) for e in graph[elem][1]) + 1
    depths[elem] = depth
    return depth

def ore_for_fuel(fuelq):
    todo = { 'FUEL': fuelq }
    while not all(k == 'ORE' for k in todo):
        deeper = max(todo, key=lambda elem: find_depth(elem))
        needed = todo[deeper]
        del todo[deeper]
        q, recipe = graph[deeper]
        nb_react = (needed - 1) // q + 1
        for elem, qe in recipe:
            todo[elem] = todo.get(elem, 0) + nb_react * qe
    return todo['ORE']

base_ore = ore_for_fuel(1)
print(base_ore)

stock = 1000000000000
inf = stock // base_ore
sup = inf * 2
while ore_for_fuel(sup) <= stock:
    inf = sup
    sup = inf * 2
while sup - inf > 1:
    mid = (inf + sup) // 2
    if ore_for_fuel(mid) <= stock:
        inf = mid
    else:
        sup = mid

print(inf)