cubes = []
for line in open('test.in'):
    if line[0:2] == 'on':
        lit = True
        line = line[3:-1]
    else:
        lit = False
        line = line[4:-1]
    cubes.append((lit, tuple(tuple(map(int, axis[2:].split('..'))) for axis in line.split(','))))

print(min(cube[1][i][0] for i in range(3) for cube in cubes))
print(max(cube[1][i][1] for i in range(3) for cube in cubes))

def remove_intersect(cube, to_remove):
    p = [[] for _ in range(3)]
    r = [0] * 3
    for i in range(3):
        if to_remove[i][0] > cube[i][1]:
            return [cube]
        if to_remove[i][0] <= cube[i][0]:
            if to_remove[i][1] < cube[i][0]:
                return [cube]
            if to_remove[i][1] >= cube[i][1]:
                p[i] = [cube[i]]
                r[i] = 0
            else:
                p[i] = [(cube[i][0], to_remove[i][1]), (to_remove[i][1] + 1, cube[i][1])]
                r[i] = 0
        else:
            p[i] = [(cube[i][0], to_remove[i][0] - 1)]
            r[i] = 1
            if to_remove[i][1] >= cube[i][1]:
                p[i].append((to_remove[i][0], cube[i][1]))
            else:
                p[i].append((to_remove[i][0], to_remove[i][1]))
                p[i].append((to_remove[i][1] + 1, cube[i][1]))
    res = []
    for x in range(len(p[0])):
        for y in range(len(p[1])):
            for z in range(len(p[2])):
                if x != r[0] or y != r[1] or z != r[2]:
                    res.append((p[0][x], p[1][y], p[2][z]))
    return res

unit_cubes = []
nb_applied = 0
for cube in cubes:
    nb_applied += 1
    if nb_applied % 10 == 0:
        print(nb_applied, 'cubes applied')
    if not cube[0]:
        unit_cubes = [c for cc in unit_cubes for c in remove_intersect(cc, cube[1])]
    else:
        to_add = [cube[1]]
        for existing in unit_cubes:
            to_add = [c for cc in to_add for c in remove_intersect(cc, existing)]
        unit_cubes += to_add

def volume(cube):
    v = 1
    for i in range(3):
        v *= cube[i][1] - cube[i][0] + 1
    return v

print(sum(volume(cube) for cube in unit_cubes), 'for', len(unit_cubes), 'unit_cubes')

# real_cubes = []
# for cube in cubes:
#     if any(cube[1][i][0] > 50 for i in range(3)) or any(cube[1][i][1] < -50 for i in range(3)):
#         continue
#     real_cubes.append((cube[0], tuple((max(-50, inf), min(50, sup)) for inf, sup in cube[1])))

# res = 0
# for x in range(-50, 51):
#     print(x)
#     for y in range(-50, 51):
#         for z in range(-50, 51):
#             p = (x, y, z)
#             is_on = False
#             for is_cube_on, cube in real_cubes:
#                 if all(cube[i][0] <= p[i] <= cube[i][1] for i in range(3)):
#                     is_on = is_cube_on
#             if is_on:
#                 res += 1

# print(res)
