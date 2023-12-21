import itertools

workflows = {}
items = []
categories = 'xmas'

for line in open('test.in'):
    line = line.rstrip()
    if not len(line):
        continue
    if line.startswith('{'):
        items.append(tuple(int(v.split('=')[1]) for v in line[1:-1].split(',')))
    else:
        p = line.index('{')
        rules = []
        for r in line[p + 1:-1].split(','):
            if ':' not in r:
                dest = r[:]
                i, cmp = 0, 0
                op = '='
            else:
                cnd, dest = r.split(':')
                i = categories.index(cnd[0])
                cmp = int(cnd[2:])
                op = cnd[1]
            rules.append((i, op, cmp, dest))
        workflows[line[:p]] = rules

def process(item):
    cur = 'in'
    while cur in workflows:
        for i, op, cmp, dest in workflows[cur]:
            if op == '=' or (op == '<' and item[i] < cmp) or (op == '>' and item[i] > cmp):
                cur = dest
                break
    return cur

res1 = 0
for item in items:
    if process(item) == 'A':
        res1 += sum(item)

print(res1)

accepted = []
todo = [('in', tuple((1, 4000) for _ in range(4)))]
while len(todo):
    next_todo = []
    for workflow, intervals in todo:
        if workflow == 'A':
            accepted.append(intervals)
            continue
        if workflow == 'R':
            continue
        for i, op, cmp, dest in workflows[workflow]:
            if op == '=':
                next_todo.append((dest, intervals))
            elif op == '<':
                if intervals[i][0] >= cmp:
                    continue
                if intervals[i][1] < cmp:
                    next_todo.append((dest, intervals))
                    break
                else:
                    next_todo.append((dest, tuple(intervals[j] if j != i else (intervals[i][0], cmp - 1) for j in range(4))))
                    intervals = tuple(intervals[j] if j != i else (cmp, intervals[i][1]) for j in range(4))
            else:
                if intervals[i][1] <= cmp:
                    continue
                if intervals[i][0] > cmp:
                    next_todo.append((dest, intervals))
                    break
                else:
                    next_todo.append((dest, tuple(intervals[j] if j != i else (cmp + 1, intervals[i][1]) for j in range(4))))
                    intervals = tuple(intervals[j] if j != i else (intervals[i][0], cmp) for j in range(4))
    todo = next_todo

res2 = 0
for it in accepted:
    for limit_item in itertools.product(*it):
        if process(limit_item) != 'A':
            raise ValueError('oups')
    p = 1
    for inf, sup in it:
        p *= sup - inf + 1
    res2 += p
print(res2)
