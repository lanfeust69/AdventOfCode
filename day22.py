boss_damage = 8

magic_missile_cost = 53
drain_cost = 73
shield_cost = 113
poison_cost = 173
recharge_cost = 229
recharge_value = 101
costs = {'Magic Missile': magic_missile_cost, 'Drain': drain_cost, 'Shield': shield_cost, 'Poison': poison_cost, 'Recharge': recharge_cost}

cache = {}
def solve(hp, mana, boss_hp, shield, poison, recharge):
    cache_key = (hp, mana, boss_hp, shield, poison, recharge)
    if cache_key in cache:
        return cache[cache_key]
    best = 1000000
    spells = []
    hp -= 1 # only for part 2
    if mana < magic_missile_cost or hp <= 0:
        # cannot cast cheapest or not enough hp : lost game
        return best, ['Magic Missile']
    if poison > 0:
        boss_hp -= 3 * min(poison, 2)
        poison -= min(poison, 2)
        if boss_hp <= 0:
            return magic_missile_cost, ['Magic Missile'] # still need to cast something
    damage = boss_damage
    if shield > 0:
        damage -= 7
        shield -= 1 # 6 turns = 3 boss attacks
    next_mana = mana
    if recharge > 0:
        next_mana += recharge_value * min(recharge, 2)
        recharge -= min(recharge, 2)
    if boss_hp <= 4:
        return magic_missile_cost, ['Magic Missile'] # cheapest spell : can't do better
    # we will be hit
    if hp + 2 > damage and mana >= drain_cost:
        sub_cost, sub_spells = solve(hp + 2 - damage, next_mana - drain_cost, boss_hp - 2, shield, poison, recharge)
        if sub_cost + drain_cost < best:
            best = sub_cost + drain_cost
            spells = ['Drain'] + sub_spells
    if shield == 0 and hp > damage - 7 and mana >= shield_cost:
        sub_cost, sub_spells = solve(hp + 7 - damage, next_mana - shield_cost, boss_hp, 2, poison, recharge)
        if sub_cost + shield_cost < best:
            best = sub_cost + shield_cost
            spells = ['Shield'] + sub_spells
    if hp <= damage:
        cache[cache_key] = best, spells
        return best, spells
    sub_cost, sub_spells = solve(hp - damage, next_mana - magic_missile_cost, boss_hp - 4, shield, poison, recharge)
    if sub_cost + magic_missile_cost < best:
        best = sub_cost + magic_missile_cost
        spells = ['Magic Missile'] + sub_spells
    if poison == 0 and mana >= poison_cost:
        sub_cost, sub_spells = solve(hp - damage, next_mana - poison_cost, boss_hp - 3, shield, 5, recharge)
        if sub_cost + poison_cost < best:
            best = sub_cost + poison_cost
            spells = ['Poison'] + sub_spells
    if recharge == 0 and mana >= recharge_cost and mana < 5000: # avoid infinite loop casting recharge
        sub_cost, sub_spells = solve(hp - damage, next_mana - recharge_cost + recharge_value, boss_hp, shield, poison, 4)
        if sub_cost + recharge_cost < best:
            best = sub_cost + recharge_cost
            spells = ['Recharge'] + sub_spells
    cache[cache_key] = best, spells
    return best, spells

def display(hp, mana, boss_hp, spells):
    turn, shield, poison, recharge = 0, 0, 0, 0
    while True:
        print(f'turn {turn}, {hp} hp, {mana} mana, boss {boss_hp}, {shield} shield, {poison} poison, {recharge} recharge')
        if poison > 0:
            boss_hp -= 3
            poison -= 1
        if recharge > 0:
            mana += recharge_value
            recharge -= 1
        if turn % 2:
            if boss_hp > 0:
                hp -= boss_damage
                if shield > 0:
                    hp += 7
        else:
            spell = spells[turn // 2]
            print('casting ', spell)
            mana -= costs[spell]
            if spell == 'Magic Missile':
                boss_hp -= 4
            elif spell == 'Drain':
                hp += 2
                boss_hp -= 2
            elif spell == 'Poison':
                poison = 6
            elif spell == 'Shield':
                shield = 6
            elif spell == 'Recharge':
                recharge = 5
            else:
                raise ValueError('unknown spell ' + spell)
        if shield > 0:
            shield -= 1
        if hp <= 0 or boss_hp <= 0:
            print(f'finished at turn {turn}, {hp} hp, {mana} mana, boss {boss_hp}, {shield} shield, {poison} poison, {recharge} recharge')
            break
        turn += 1

total, spells = solve(50, 500, 55, 0, 0, 0)
display(50, 500, 55, spells)
print(total)
