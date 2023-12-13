from collections import Counter

hands1 = []
hands2 = []
rank1 = {str(i): i for i in range(2, 10)}
rank1 |= {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
rank2 = dict(rank1)
rank2['J'] = 1
for line in open('test.in'):
    hand, bid = line.rstrip().split()
    hand1 = [rank1[c] for c in hand]
    hand2 = [rank2[c] for c in hand]
    bid = int(bid)
    hands1.append((hand1, bid))
    hands2.append((hand2, bid))

def value(hand, with_joker=False):
    c = Counter(hand)
    nb_joker = 0
    if with_joker and 1 in c:
        nb_joker = c[1]
        del c[1]
    if nb_joker == 5:
        return 7, hand
    cc = [count for _, count in c.items()]
    cc.sort(reverse=True)
    cc[0] += nb_joker
    if cc[0] == 5:
        return 7, hand
    if cc[0] == 4:
        return 6, hand
    if cc[0] == 3 and cc[1] == 2:
        return 5, hand
    if cc[0] == 3:
        return 4, hand
    if cc[0] == 2 and cc[1] == 2:
        return 3, hand
    if cc[0] == 2:
        return 2, hand
    return 1, hand

hands1.sort(key=lambda h: value(h[0]))
hands2.sort(key=lambda h: value(h[0], True))
print(sum(hand[1] * (i + 1) for i, hand in enumerate(hands1)))
print(sum(hand[1] * (i + 1) for i, hand in enumerate(hands2)))
