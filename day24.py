comps = [tuple(map(int, line.rstrip().split('/'))) for line in open('test.in')]
strengths = [sum(comp) for comp in comps]

reachable = {0: set([0])}

to_check = [(0, 0)]
while len(to_check) > 0:
    next_to_check = []
    for end, used in to_check:
        for i in range(len(comps)):
            if (1 << i) & used == 0 and end in comps[i]:
                new_used = used | (1 << i)
                other = comps[i][1 if end == comps[i][0] else 0]
                if other in reachable and new_used in reachable[other]:
                    continue
                progress = True
                if other in reachable:
                    reachable[other].add(new_used)
                else:
                    reachable[other] = set([new_used])
                next_to_check.append((other, new_used))
    to_check = next_to_check

def compute_length_strength(used):
    length, strength = 0, 0
    for i in range(len(comps)):
        if (1 << i) & used == 0:
            continue
        length += 1
        strength += strengths[i]
    return length, strength

print(max(max(compute_length_strength(used)[1] for used in ways) for ways in reachable.values()))
print(max(max(compute_length_strength(used) for used in ways) for ways in reachable.values()))
