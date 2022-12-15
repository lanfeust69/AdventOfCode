import itertools

def parse(line):
    costs = []
    for r in line.split(': ')[1].split('.')[:-1]: # [:-1] to skip empty last (final '.')
        words = r.split()
        if words[1] == 'ore' or words[1] == 'clay':
            costs.append([int(words[4]), 0, 0])
        elif words[1] == 'obsidian':
            costs.append([int(words[4]), int(words[7]), 0])
        else:
            costs.append([int(words[4]), 0, int(words[7])])
    return costs

blueprints = [parse(line.rstrip()) for line in open('test.in')]
b = 0
max_time = 23

def evaluate(blueprint):
    cache = {}
    def find_best(time, nb_robots, nb_resource):
        if time == max_time:
            return nb_robots[3]
        cache_key = time, nb_robots, nb_resource
        if cache_key in cache:
            return cache[cache_key]
        can_build = [all(nb_resource[i] >= blueprint[j][i] for i in range(3)) for j in range(4)]
        enough_ore_robots = all(blueprint[j][0] <= nb_robots[0] for j in range(3))
        if enough_ore_robots:
            can_build[0] = False
        enough_clay_robots = blueprint[2][1] <= nb_robots[1]
        if enough_clay_robots:
            can_build[1] = False
        enough_obs_robots = blueprint[3][2] <= nb_robots[2]
        if enough_obs_robots:
            can_build[2] = False
        best = 0
        # always build something if all can be built up to most "advanced" that we have none of :
        must_build = False
        if can_build[0] and can_build[1]:
            if nb_robots[1] == 0:
                must_build = True
            elif can_build[2]:
                if nb_robots[2] == 0 or can_build[3]:
                    must_build = True
        if enough_obs_robots and can_build[3]:
            must_build = True
        if enough_ore_robots and enough_clay_robots and can_build[2] and can_build[3]:
            must_build = True
        if not must_build:
            new_resources = tuple(nb_resource[i] + nb_robots[i] for i in range(3))
            new_robots = nb_robots
            best = find_best(time + 1, new_robots, new_resources) + nb_robots[3]
        for build in range(4):
            if not can_build[build]:
                continue
            new_resources = tuple(nb_resource[i] - blueprint[build][i] + nb_robots[i] for i in range(3))
            new_robots = tuple(nb_robots[i] + (i == build) for i in range(4))
            best = max(best, find_best(time + 1, new_robots, new_resources) + nb_robots[3])
        cache[cache_key] = best
        if len(cache) % 1000000 == 0:
            print('cache has now', len(cache), 'entries')
        return best
    global b
    b += 1
    print('blueprint', b)
    res = find_best(0, (1, 0, 0, 0), (0, 0, 0))
    print('best is', res, 'found with', len(cache), 'entries in the cache')
    return res

print(sum((i + 1) * evaluate(blueprints[i]) for i in range(len(blueprints))))
max_time = 31
b = 0
three_first = [evaluate(blueprints[i]) for i in range(3)]
print(three_first)
res = 1
for v in three_first:
    res *= v
print(res)
