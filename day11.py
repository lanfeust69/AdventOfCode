monkeys_inventories = []
monkeys_opes = []
monkeys_actions = []

for line in open('test.in'):
    if line.startswith('Monkey'):
        continue
    if line.startswith('  Starting items: '):
        monkeys_inventories.append(list(map(int, line[len('  Starting items: '):].split(', '))))
    if line.startswith('  Operation: new = '):
        monkeys_opes.append(line[len('  Operation: new = '):])
    if line.startswith('  Test: divisible by '):
        cur_div = int(line[len('  Test: divisible by '):])
    if line.startswith('    If true: throw to monkey '):
        cur_true = int(line[len('    If true: throw to monkey '):])
    if line.startswith('    If false: throw to monkey '):
        cur_false = int(line[len('    If false: throw to monkey '):])
        monkeys_actions.append((cur_div, cur_true, cur_false))

counts = [0] * len(monkeys_inventories)
mod = 1
for div, _, _ in monkeys_actions:
    mod *= div

for _ in range(10000):
    for monkey in range(len(monkeys_inventories)):
        for item in monkeys_inventories[monkey]:
            counts[monkey] += 1
            old = item
            new_val = eval(monkeys_opes[monkey]) % mod
            div, if_true, if_false = monkeys_actions[monkey]
            monkeys_inventories[if_true if new_val % div == 0 else if_false].append(new_val)
        monkeys_inventories[monkey].clear()

counts.sort()
print(counts[-1] * counts[-2])
