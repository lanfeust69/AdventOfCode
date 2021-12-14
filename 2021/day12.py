graph = {}
for line in open('test.in'):
    a, b = line[:-1].split('-')
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

small = [cave for cave in graph if cave.lower() == cave and cave != 'start' and cave != 'end']
small_ids = {small[i]: i + 1 for i in range(len(small))}

start_state = tuple(['start'] + [0] * len(small))
todo = [start_state]

def neighbors(state):
    for neigh in graph[state[0]]:
        if neigh == 'start':
            continue
        if neigh not in small:
            yield tuple([neigh] + list(state[1:]))
        else:
            small_id = small_ids[neigh]
            if state[small_id] == 0 or (state[small_id] == 1 and all(state[i] < 2 for i in range(1, len(state)))):
                yield tuple([neigh] + [state[i] + (1 if i == small_id else 0) for i in range(1, len(state))])

res = 0
while len(todo) > 0:
    next_todo = []
    for state in todo:
        for neigh in neighbors(state):
            if neigh[0] == 'end':
                res += 1
            else:
                next_todo.append(neigh)
    todo = next_todo

print(res)
