deck1 = []
deck2 = []
cur_deck = deck1
for line in open('test.in'):
    line = line[:-1]
    if line == 'Player 1:' or line == '':
        continue
    if line == 'Player 2:':
        cur_deck = deck2
        continue
    cur_deck.append(int(line))

def play(deck1, deck2, rec):
    seen = set()
    while len(deck1) > 0 and len(deck2) > 0:
        key = (tuple(deck1), tuple(deck2))
        if key in seen:
            return 1, deck1
        seen.add(key)
        c1, c2 = deck1[0], deck2[0]
        deck1 = deck1[1:]
        deck2 = deck2[1:]
        if rec and c1 <= len(deck1) and c2 <= len(deck2):
            winner, _ = play(deck1[:c1], deck2[:c2], rec)
        else:
            winner = 1 if c1 > c2 else 2
        if winner == 1:
            deck1 += [c1, c2]
        else:
            deck2 += [c2, c1]
    return (1, deck1) if len(deck1) > 0 else (2, deck2)

_, winner_deck = play(deck1[:], deck2[:], False)
print(sum(i * winner_deck[-i] for i in range(1, len(winner_deck) + 1)))
_, winner_deck = play(deck1[:], deck2[:], True)
print(sum(i * winner_deck[-i] for i in range(1, len(winner_deck) + 1)))
