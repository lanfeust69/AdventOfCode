from functools import cache

# stones = [125, 17]
stones = [814, 1183689, 0, 1, 766231, 4091, 93836, 46]

@cache
def nb_after(initial, nb_blinks):
    if nb_blinks == 0:
        return 1
    if initial == 0:
        return nb_after(1, nb_blinks - 1)
    s = str(initial)
    if len(s) % 2 == 0:
        return nb_after(int(s[:len(s) // 2]), nb_blinks - 1) + nb_after(int(s[len(s) // 2:]), nb_blinks - 1)
    return nb_after(initial * 2024, nb_blinks - 1)

print(sum(nb_after(stone, 75) for stone in stones))
