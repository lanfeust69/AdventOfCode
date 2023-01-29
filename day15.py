part2 = False

def gen():
    # a, b = 65, 8921
    a, b = 591, 393
    while True:
        a = a * 16807 % 2147483647
        b = b * 48271 % 2147483647
        if part2:
            while a % 4 != 0:
                a = a * 16807 % 2147483647
            while b % 8 != 0:
                b = b * 48271 % 2147483647
        yield a, b

for part in range(2):
    nb = 5000000 if part else 40000000
    part2 = part
    i = 0
    nb_match = 0
    mask = (1 << 16) - 1
    for a, b in gen():
        if a & mask == b & mask:
            nb_match += 1
        i += 1
        if i == nb:
            break

    print(nb_match)
