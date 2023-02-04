nb_players, last_marble = 438, 7162600

links = [[0, 0]] * (last_marble + 1)
cur = 0
player = 0
scores = [0] * nb_players

for marble in range(1, last_marble + 1):
    if marble % 1000000 == 0:
        print(marble)
    if marble % 23 == 0:
        score = marble
        for _ in range(7):
            cur = links[cur][1]
        score += cur
        scores[player] += score
        links[links[cur][0]][1] = links[cur][1]
        links[links[cur][1]][0] = links[cur][0]
        cur = links[cur][0]
    else:
        cur = links[cur][0]
        succ = links[cur][0]
        links[marble] = [succ, cur]
        links[cur][0] = marble
        links[succ][1] = marble
        cur = marble
    player = (player + 1) % nb_players

print(max(scores))
