res = 0
for line in open('test.in'):
    parts = line.rstrip().split('-')
    id, ck = parts[-1][:-1].split('[')
    id = int(id)
    counts = {}
    decrypted = []
    for part in parts[:-1]:
        decrypt = ''
        for c in part:
            if ord(c) >= ord('a'):
                decrypt += chr(ord('a') + (ord(c) - ord('a') + id) % 26)
            else:
                decrypt += chr(ord('A') + (ord(c) - ord('A') + id) % 26)
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
        decrypted.append(decrypt)
    checksum = ''.join(p[1] for p in sorted((-count, c) for c, count in counts.items())[:5])
    if 'northpole' in decrypted:
        print('North Pole object are in room', id)
    if ck == checksum:
        # if 'North' in decrypted and 'Pole' in decrypted:
        res += id

print(res)
