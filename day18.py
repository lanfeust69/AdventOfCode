all_cubes = [tuple(map(int, line.rstrip().split(','))) for line in open('test.in')]

def area(cubes):
    by_pair = [{} for _ in range(3)]
    total = 0
    for cube in cubes:
        total += 6
        for i in range(3):
            key = cube[:i] + cube[i + 1:]
            if key in by_pair[i]:
                by_pair[i][key].append(cube[i])
            else:
                by_pair[i][key] = [cube[i]]

    for i in range(3):
        for v in by_pair[i].values():
            v.sort()
            for j in range(1, len(v)):
                if v[j] == v[j - 1] + 1:
                    total -= 2
    return total

total = area(all_cubes)
print(total)

enclosing = [0] * 3
for cube in all_cubes:
    for i in range(3):
        if cube[i] < 0:
            raise ValueError('not all > 0')
        enclosing[i] = max(enclosing[i], cube[i])
for i in range(3):
    enclosing[i] += 1

big_cube = [[[False] * enclosing[2] for _ in range(enclosing[1])] for _ in range(enclosing[0])]
for cube in all_cubes:
    big_cube[cube[0]][cube[1]][cube[2]] = True
visited = [[[False] * enclosing[2] for _ in range(enclosing[1])] for _ in range(enclosing[0])]
neigh_dir = []
for i in range(3):
    neigh_dir.append((0,) * i + (1,) + (0,) * (2 - i))
    neigh_dir.append((0,) * i + (-1,) + (0,) * (2 - i))
for x in range(enclosing[0]):
    for y in range(enclosing[1]):
        for z in range(enclosing[2]):
            if visited[x][y][z] or big_cube[x][y][z]:
                continue
            touches_outside = False
            component = [(x, y, z)]
            visited[x][y][z] = True
            todo = [(x, y, z)]
            while len(todo) > 0:
                next_todo = []
                for p in todo:
                    for dx, dy, dz in neigh_dir:
                        pp = p[0] + dx, p[1] + dy, p[2] + dz
                        is_outside = False
                        for i in range(3):
                            if pp[i] < 0 or pp[i] >= enclosing[i]:
                                is_outside = True
                                break
                        if is_outside:
                            touches_outside = True
                            continue
                        if visited[pp[0]][pp[1]][pp[2]] or big_cube[pp[0]][pp[1]][pp[2]]:
                            continue
                        component.append(pp)
                        next_todo.append(pp)
                        visited[pp[0]][pp[1]][pp[2]] = True
                todo = next_todo
            if not touches_outside:
                total -= area(component)

print(total)
