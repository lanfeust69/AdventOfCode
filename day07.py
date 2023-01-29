puzzle = {}

for line in open('test.in'):
    tokens = line.rstrip().split()
    a, b = tokens[1], tokens[-3]
    if a not in puzzle:
        puzzle[a] = set()
    if b not in puzzle:
        puzzle[b] = set([a])
    else:
        puzzle[b].add(a)

reqs = {p: set(puzzle[p]) for p in puzzle}
res = ''
while len(reqs) > 0:
    todo = min(r for r in reqs if len(reqs[r]) == 0)
    res += todo
    for r in reqs:
        reqs[r].discard(todo)
    del reqs[todo]

print(res)

nb_available = 5
free = []
t = 0
reqs = {p: set(puzzle[p]) for p in puzzle}
running = set()
res = ''
while len(reqs) > 0:
    todos = [r for r in reqs if len(reqs[r]) == 0 and r not in running]
    if nb_available == 0 or len(todos) == 0:
        t = free[0][0]
        while len(free) > 0 and free[0][0] == t:
            nb_available += 1
            done = free[0][1]
            for r in reqs:
                reqs[r].discard(done)
            free = free[1:]
            del reqs[done]
            running.remove(done)
        continue
    todos.sort()
    for i in range(min(nb_available, len(todos))):
        nb_available -= 1
        todo = todos[i]
        running.add(todo)
        free.append((t + ord(todo) - 4, todo))
        free.sort()

print(t)
