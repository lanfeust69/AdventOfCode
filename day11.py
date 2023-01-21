# nb_elems = 2
# floors = [
#     ((0, 1), ()),
#     ((), (0,)),
#     ((), (1,)),
#     ((), ())
# ]
nb_elems = 7
floors = [
    # ((0, 1, 2), (0, 1, 2, 3, 4)),
    ((0, 1, 2, 5, 6), (0, 1, 2, 3, 4, 5, 6)),
    ((3, 4), ()),
    ((), ()),
    ((), ())
]

initial_state = (0, tuple(floors))

def neighbors(state):
    start, floors = state
    chips, rtgs = floors[start]
    moves = []
    for i in range(len(chips)):
        chip = chips[i]
        moves.append(((chip,), ()))
        if chip in rtgs:
            moves.append(((chip,), (chip,)))
        for j in range(i + 1, len(chips)):
            moves.append(((chip, chips[j]), ()))
    for i in range(len(rtgs)):
        rtg = rtgs[i]
        if rtg not in chips or len(rtgs) == 1:
            moves.append(((), (rtg,)))
        for j in range(i + 1, len(rtgs)):
            if (rtg not in chips and rtgs[j] not in chips) or len(rtgs) == 2:
                moves.append(((), (rtg, rtgs[j])))
    for delta in [-1, 1] if 0 < start < 3 else ([1] if start == 0 else [-1]):
        for c, r in moves:
            dest = start + delta
            new_dest_chips = tuple(i for i in range(nb_elems) if i in floors[dest][0] or i in c)
            new_dest_rtgs = tuple(i for i in range(nb_elems) if i in floors[dest][1] or i in r)
            if len(new_dest_rtgs) > 0 and any(i not in new_dest_rtgs for i in new_dest_chips):
                continue
            new_start_chips = tuple(i for i in range(nb_elems) if i in floors[start][0] and i not in c)
            new_start_rtgs = tuple(i for i in range(nb_elems) if i in floors[start][1] and i not in r)
            yield dest, tuple((new_start_chips, new_start_rtgs) if i == start else ((new_dest_chips, new_dest_rtgs) if i == dest else floors[i]) for i in range(4))

final_state = (3, (((), ()), ((), ()), ((), ()), (tuple(range(nb_elems)), tuple(range(nb_elems)))))
todo = [initial_state]
seen = {initial_state: None}
step = 0
found = False
while not found and len(todo) > 0:
    step += 1
    next_todo = []
    for state in todo:
        for neigh in neighbors(state):
            if neigh in seen:
                continue
            seen[neigh] = state
            elevator, floors = neigh
            if neigh == final_state:
                print(step)
                found = True
                break
            next_todo.append(neigh)
        if found:
            break
    todo = next_todo

def display(state):
    elevator, floors = state
    for floor in range(3, -1, -1):
        print(('* [' if elevator == floor else '  [') + ' '.join(str(i) if i in floors[floor][0] else ' ' for i in range(nb_elems)) + '] [' + ' '.join(str(i) if i in floors[floor][1] else ' ' for i in range(nb_elems)) + ']')

# to_print = [final_state]
# while to_print[-1] != initial_state:
#     to_print.append(seen[to_print[-1]])
# to_print.reverse()
# for state in to_print:
#     display(state)
#     print()
