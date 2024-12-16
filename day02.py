def is_safe(report):
    deltas = [report[i] - report[i - 1] for i in range(1, len(report))]
    return all(1 <= delta <= 3 for delta in deltas) or all(-3 <= delta <= -1 for delta in deltas)

def is_safe2(report):
    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1:]):
            return True
    return False

res1, res2 = 0, 0

for line in open('test.in'):
    line = line.rstrip()
    report = list(map(int, line.split()))
    if is_safe(report):
        res1 += 1
    if is_safe2(report):
        res2 += 1

print(res1)
print(res2)
