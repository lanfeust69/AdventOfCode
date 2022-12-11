deers = []
for line in open('test.in'):
    parts = line.split()
    deers.append((int(parts[3]), int(parts[6]), int(parts[-2])))

res = 0
race_time = 2503
for deer in deers:
    t = deer[1] + deer[2]
    dist = race_time // t * deer[0] * deer[1]
    dist += min(deer[1], race_time % t) * deer[0]
    res = max(res, dist)

print(res)

deers_pos = [0] * len(deers)
deers_score = [0] * len(deers)
for t in range(race_time):
    for d in range(len(deers)):
        if t % (deers[d][1] + deers[d][2]) < deers[d][1]:
            deers_pos[d] += deers[d][0]
    leader_pos = max(deers_pos)
    for d in range(len(deers)):
        if deers_pos[d] == leader_pos:
            deers_score[d] += 1

print(max(deers_score))
