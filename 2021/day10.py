closing = {')': '(', ']': '[', '}': '{', '>': '<'}
# costs = {')': 3, ']': 57, '}': 1197, '>': 25137}
costs = {'(': 1, '[': 2, '{': 3, '<': 4}

completion_costs = []
for line in open('test.in'):
    line = line[:-1]
    stack = []
    ok = True
    for c in line:
        if c in closing:
            if len(stack) == 0 or stack.pop() != closing[c]:
                ok = False
                break
        else:
            stack.append(c)
    if not ok:
        continue
    s = 0
    while len(stack) > 0:
        s = s * 5 + costs[stack.pop()]
    completion_costs.append(s)

completion_costs.sort()
print(completion_costs[len(completion_costs) // 2])
