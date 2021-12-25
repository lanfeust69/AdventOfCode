import heapq

# start = (tuple([0] * 7), ((2, 1), (3, 4), (2, 3), (4, 1)))
# start = (tuple([0] * 7), ((2, 4, 4, 1), (3, 3, 2, 4), (2, 2, 1, 3), (4, 1, 3, 1)))
start = (tuple([0] * 7), ((4, 4, 4, 3), (3, 3, 2, 4), (1, 2, 1, 1), (2, 1, 3, 2)))
room_size = len(start[1][1])
end = (tuple([0] * 7), tuple(tuple(i + 1 for _ in range(room_size)) for i in range(4)))
costs = [1, 10, 100, 1000]

distances = {start: 0}
heap = []
heapq.heappush(heap, (0, start))

def neighbors(pos):
    hallway, rooms = pos
    # if one in the hall can reach its room, will be needed eventually at same cost
    # so might as well do it now -> only move to consider
    for i in range(7):
        pod = hallway[i]
        if pod == 0:
            continue
        target = rooms[pod - 1]
        if any(x != 0 and x != pod for x in target):
            continue
        # left an right positions of the hallway above a room 
        l, r = pod, pod + 1
        to, delta = (l, 1) if i <= l else (r, -1)
        ok = True
        cost = 0
        for j in range(i + delta, to + delta, delta):
            if hallway[j] != 0:
                ok = False
                break
            cost += costs[pod - 1] * (2 if j != 1 and j != 5 else 1)
        if not ok:
            continue
        hallway = hallway[:i] + (0, ) + hallway[i + 1:]
        for r in range(room_size):
            if target[r] == 0 and (r == room_size - 1 or target[r + 1] != 0):
                break
        cost += costs[pod - 1] * (2 + r)
        rooms = rooms[:pod - 1] + (tuple([0] * r + [pod] * (room_size - r)) ,) + rooms[pod:]
        yield (hallway, rooms), cost
        return
    for i in range(4):
        if all(x == 0 or x == i + 1 for x in rooms[i]):
            continue
        for j in range(room_size):
            if rooms[i][j] == 0:
                continue
            pod = rooms[i][j]
            initial_cost = costs[pod - 1] * (2 + j)
            final_room = tuple(0 for _ in range(j + 1)) + rooms[i][j + 1:]
            break
        for dir, dest in [(-1, i + 1), (1, i + 2)]:
            cost = initial_cost
            while dest >= 0 and dest < 7 and hallway[dest] == 0:
                yield (hallway[:dest] + (pod, ) + hallway[dest + 1:], rooms[:i] + (final_room, ) + rooms[i + 1:]), cost
                dest += dir
                cost += costs[pod - 1] * (1 if dest == 0 or dest == 6 else 2)

while True:
    d, pos = heapq.heappop(heap)
    if pos == end:
        print(d)
        break
    if distances[pos] < d:
        continue
    for neigh, cost in neighbors(pos):
        if neigh not in distances or d + cost < distances[neigh]:
            distances[neigh] = d + cost
            heapq.heappush(heap, (d + cost, neigh))
