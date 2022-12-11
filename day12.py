import json

for line in open('test.in'):
    val = json.loads(line)

def sum_ints(j):
    if isinstance(j, int):
        return j
    if isinstance(j, list):
        return sum(sum_ints(x) for x in j)
    if isinstance(j, dict):
        if 'red' in j.values():
            return 0
        else:
            return sum(sum_ints(x) for x in j.values())
    return 0

print(sum_ints(val))
