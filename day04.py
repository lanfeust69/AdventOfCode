total_sleep = {}
sleeping_minutes = {}
lines = [line.rstrip() for line in open('test.in')]
lines.sort()
cur = ''
start = -1
for line in lines:
    if 'begins shift' in line:
        cur = line.split()[-3]
        if cur not in total_sleep:
            total_sleep[cur] = 0
            sleeping_minutes[cur] = [0] * 60
    elif 'falls asleep' in line:
        start = int(line.split()[1][3:5])
    elif 'wakes up' in line:
        end = int(line.split()[1][3:5])
        total_sleep[cur] += end - start
        for i in range(start, end):
            sleeping_minutes[cur][i] += 1

max_sleep = 0
max_time = 0
target1, minute1 = -1, -1
target2, minute2 = -1, -1
for guard in total_sleep:
    if total_sleep[guard] > max_sleep:
        max_sleep = total_sleep[guard]
        minute1 = sleeping_minutes[guard].index(max(sleeping_minutes[guard]))
        target1 = guard
    for m in range(60):
        if sleeping_minutes[guard][m] > max_time:
            max_time = sleeping_minutes[guard][m]
            target2 = guard
            minute2 = m

print(target1, minute1, int(target1[1:]) * minute1)
print(target2, minute2, int(target2[1:]) * minute2)
