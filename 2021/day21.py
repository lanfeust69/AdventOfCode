p1, p2 = 5, 9
s1, s2 = 0, 0
d = 0
nb_roll = 0
def roll():
    global d, nb_roll
    s = 0
    for _ in range(3):
        s += d
        d = (d + 1) % 100
    nb_roll += 3
    return s + 3

while True:
    p1 = (p1 + roll()) % 10
    s1 += p1 + 1
    if s1 >= 1000:
        print(s2 * nb_roll)
        break
    p2 = (p2 + roll()) % 10
    s2 += p2 + 1
    if s2 >= 1000:
        print(s1 * nb_roll)
        break

dirac_rolls = {i: 0 for i in range(3, 10)}
for d1 in range(1, 4):
    for d2 in range(1, 4):
        for d3 in range(1, 4):
            dirac_rolls[d1 + d2 + d3] += 1

cache = {}
def count_wins(key):
    if key in cache:
        return cache[key]
    p1, p2, s1, s2, is_p1_turn = key
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)
    win1, win2 = 0, 0
    for roll, nb in dirac_rolls.items():
        if is_p1_turn:
            w1, w2 = count_wins(((p1 + roll) % 10, p2, s1 + (p1 + roll) % 10 + 1, s2, False))
        else:
            w1, w2 = count_wins((p1, (p2 + roll) % 10, s1, s2 + (p2 + roll) % 10 + 1, True))
        win1 += w1 * nb
        win2 += w2 * nb
    cache[key] = (win1, win2)
    return win1, win2

print(count_wins((3, 7, 0, 0, True)))
print(count_wins((5, 9, 0, 0, True)))
