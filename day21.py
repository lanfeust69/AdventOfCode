import itertools

weapons = [(4 + i, c) for i, c in enumerate([8, 10, 25, 40, 74])]
armors = [(i, c) for i, c in enumerate([0, 13, 31, 53, 75, 102])]
attack_rings = [(i + 1, c) for i, c in enumerate([25, 50, 100])]
defense_rings = [(i + 1, c) for i, c in enumerate([20, 40, 80])]

boss_hp = 109
boss_damage = 8
boss_armor = 2

my_hp = 100

best1 = 10000
best2 = 0

for choice in itertools.product(range(len(weapons)), range(len(armors)), range(1 << len(attack_rings)), range(1 << len(defense_rings))):
    damage = weapons[choice[0]][0]
    cost = weapons[choice[0]][1]
    armor = armors[choice[1]][0]
    cost += armors[choice[1]][1]
    for i in range(len(attack_rings)):
        if choice[2] & (1 << i):
            damage += attack_rings[i][0]
            cost += attack_rings[i][1]
    for i in range(len(defense_rings)):
        if choice[3] & (1 << i):
            armor += defense_rings[i][0]
            cost += defense_rings[i][1]
    effective_damage = max(1, damage - boss_armor)
    nb_kill = (boss_hp - 1) // effective_damage + 1
    effective_boss_damage = max(1, boss_damage - armor)
    if (nb_kill - 1) * effective_boss_damage < my_hp:
        best1 = min(best1, cost)
    else:
        best2 = max(best2, cost)

print(best1, best2)
