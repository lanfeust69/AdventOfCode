units_base = []
in_immune = True
for line in open('test.in'):
    line = line.rstrip()
    if 'Immune System:' in line:
        in_immune = True
        continue
    if 'Infection:' in line:
        in_immune = False
        continue
    if len(line) == 0:
        continue
    if '(' in line:
        s, e = line.index('('), line.index(')')
        mid = line[s + 1:e]
        if ';' in mid:
            a, b = mid.split('; ')
            resist_str, weak_str = (a, b) if a.startswith('immune') else (b, a)
        elif mid.startswith('immune'):
            resist_str, weak_str = mid, ''
        else:
            resist_str, weak_str = '', mid
        tokens = line[:s].split() + line[e + 1:].split()
    else:
        resist_str, weak_str = '', ''
        tokens = line.split()
    nb, hp = int(tokens[0]), int(tokens[4])
    damage, damage_type = int(tokens[-6]), tokens[-5]
    initiative = int(tokens[-1])
    resist, weak = [], []
    if len(resist_str) > 0:
        resist = resist_str[10:].split(', ')
    if len(weak_str) > 0:
        weak = weak_str[8:].split(', ')
    units_base.append([initiative, in_immune, nb, hp, damage, damage_type, resist, weak])

units_base.sort(reverse=True)

def solve(units):
    immune_win = False
    while True:
        immune, infect = [], []
        for i in range(len(units)):
            if units[i][2] == 0:
                continue
            if units[i][1]:
                immune.append(i)
            else:
                infect.append(i)
        if len(immune) == 0 or len(infect) == 0:
            immune_win = len(immune) > 0
            break
        for cur in [immune, infect]:
            cur.sort(key=lambda i: (units[i][2] * units[i][4], units[i][0]), reverse=True)
        immune_targets, infect_targets = [], []
        for cur in [immune, infect]:
            if cur == immune:
                opp = infect
                targets = immune_targets
            else:
                opp = immune
                targets = infect_targets
            chosen = [False] * len(opp)
            for i in cur:
                best, best_damage = -1, 0
                damage, damage_type = units[i][4], units[i][5]
                for j in range(len(opp)):
                    if chosen[j]:
                        continue
                    if damage_type in units[opp[j]][6]:
                        continue
                    coef = 1
                    if damage_type in units[opp[j]][7]:
                        coef = 2
                    if damage * coef > best_damage:
                        best_damage = damage * coef
                        best = j
                targets.append((opp[best], best_damage))
                if best != -1:
                    chosen[best] = True
        total_killed = 0
        for i in range(len(units)):
            if units[i][2] == 0:
                continue
            if i in immune:
                target, damage = immune_targets[immune.index(i)]
            else:
                target, damage = infect_targets[infect.index(i)]
            total_damage = units[i][2] * damage
            nb_killed = total_damage // units[target][3]
            total_killed += nb_killed
            units[target][2] = max(0, units[target][2] - nb_killed)
        if total_killed == 0:
            break

    survivors = sum(unit[2] for unit in units)
    return immune_win, survivors

_, part1 = solve([unit[:] for unit in units_base])
print(part1)

def with_boost(boost):
    units = [unit[:] for unit in units_base]
    for unit in units:
        if unit[1]:
            unit[4] += boost
    return solve(units)

inf = 0
sup = 1000
while not with_boost(sup)[0]:
    sup *= 2

res = 0
while inf + 1 < sup:
    mid = (inf + sup) // 2
    ok, survivors = with_boost(mid)
    if ok:
        res = survivors
        sup = mid
    else:
        inf = mid

print(res)
