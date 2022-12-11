res1, res2 = 0, 0
vowels = 'aeiou'
bad = {'a': 'b', 'c': 'd', 'p': 'q', 'x': 'y'}
for line in open('test.in'):
    line = line.rstrip()
    has_doubled = False
    has_bad = False
    nb_vowels = int(line[0] in vowels)
    pairs = {}
    has_pair = False
    has_one_repeat = False
    for i in range(1, len(line)):
        nb_vowels += line[i] in vowels
        if line[i] == line[i - 1]:
            has_doubled = True
        if line[i - 1] in bad and bad[line[i - 1]] == line[i]:
            has_bad = True
        pair = line[i - 1: i + 1]
        if pair in pairs:
            if pairs[pair] != i - 2:
                has_pair = True
        else:
            pairs[pair] = i - 1
        if i > 1 and line[i - 2] == line[i]:
            has_one_repeat = True
        
    if has_doubled and nb_vowels >= 3 and not has_bad:
        res1 += 1
    if has_pair and has_one_repeat:
        res2 += 1

print(res1, res2)
