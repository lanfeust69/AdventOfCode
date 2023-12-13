colors = {'red': 0, 'green': 1, 'blue': 2}
games = {}
for line in open('test.in'):
    id, draws = line.split(': ')
    id = int(id[5:])
    game_draws = []
    for draw in draws.split('; '):
        c = [0] * 3
        for cubes in draw.split(', '):
            for color, idx in colors.items():
                if color in cubes:
                    c[idx] = int(cubes[:-len(color) - 1])
                    break
        game_draws.append(c)
    games[id] = game_draws

nb_cubes = [12, 13, 14]
res1, res2 = 0, 0
for id, draws in games.items():
    if all(all(draw[i] <= nb_cubes[i] for i in range(3)) for draw in draws):
        res1 += id
    min_set = [max(draw[i] for draw in draws) for i in range(3)]
    res2 += min_set[0] * min_set[1] * min_set[2]

print(res1)
print(res2)
