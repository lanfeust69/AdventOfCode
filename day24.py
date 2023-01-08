import functools

weights = [int(line.rstrip()) for line in open('test.in')]
# weights = list(range(1, 6)) + list(range(7, 12))
n = len(weights)

print(sum(weights))
# target = sum(weights) // 3
target = sum(weights) // 4

weights.sort(reverse=True)

def can_split_in_2(to_split):
    nb_first_half = len(to_split) // 2
    first_half = set()
    for i in range(1 << nb_first_half):
        s = 0
        for j in range(nb_first_half):
            if i & (1 << j):
                s += to_split[j]
        first_half.add(s)
    nb_second_half = len(to_split) - nb_first_half
    for i in range(1 << nb_second_half):
        s = 0
        for j in range(nb_second_half):
            if i & (1 << j):
                s += to_split[nb_first_half + j]
        if target - s in first_half:
            return True
    return False

def can_split_in_3(to_split):
    nb_first_half = len(to_split) // 2
    first_half = {}
    for i in range(1 << nb_first_half):
        s = 0
        for j in range(nb_first_half):
            if i & (1 << j):
                s += to_split[j]
        if s in first_half:
            first_half[s].append(i)
        else:
            first_half[s] = [i]
    nb_second_half = len(to_split) - nb_first_half
    for i in range(1 << nb_second_half):
        s = 0
        for j in range(nb_second_half):
            if i & (1 << j):
                s += to_split[nb_first_half + j]
        if target - s in first_half:
            for used1 in first_half[target - s]:
                remain = [weights[j] for j in range(nb_first_half) if not (used1 & (1 << j))]
                remain += [weights[nb_first_half + j] for j in range(nb_second_half) if not (i & (1 << j))]
                if can_split_in_2(remain):
                    return True
    return False

# greedily take biggest first to trim when bigger than best up to now
min_nb = n
def choices(pos, nb_used, cur):
    global min_nb
    if cur == 0:
        min_nb = min(nb_used, min_nb)
        yield 0
    if pos == n or nb_used > min_nb:
        return
    if cur >= weights[pos]:
        for sub in choices(pos + 1, nb_used + 1, cur - weights[pos]):
            yield (1 << pos) | sub
    # should usually shortcut quickly
    for sub in choices(pos + 1, nb_used, cur):
        yield sub

min_possible, min_entangle = n, functools.reduce(lambda a, b: a * b, weights, 1)
for used in choices(0, 0, target):
    choice = [weights[i] for i in range(n) if used & (1 << i)]
    if len(choice) > min_possible:
        continue
    to_split = [weights[i] for i in range(n) if not (used & (1 << i))]
    # if not can_split_in_2(to_split):
    if not can_split_in_3(to_split):
        continue
    entangle = functools.reduce(lambda a, b: a * b, choice, 1)
    if len(choice) < min_possible or entangle < min_entangle:
        min_possible = len(choice)
        min_entangle = entangle

print(min_entangle)
