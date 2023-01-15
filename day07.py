def is_tls_or_ssl(s):
    brackets = 0
    not_tls = False
    tls = False
    ssl = False
    abas = set()
    babs = set()
    for i in range(len(s) - 2):
        if s[i] == '[':
            brackets += 1
        elif s[i] == ']':
            brackets -= 1
        else:
            if i + 3 < len(s):
                is_abba = s[i] != s[i + 1] and s[i + 1] not in '[]' and s[i + 1] == s[i + 2] and s[i] == s[i + 3]
                if is_abba:
                    if brackets > 0:
                        not_tls = True
                    else:
                        tls = True
            if s[i] == s[i + 2] and s[i + 1] != s[i] and s[i + 1] not in '[]':
                if brackets > 0:
                    if (s[i + 1], s[i]) in abas:
                        ssl = True
                    babs.add((s[i], s[i + 1]))
                else:
                    if (s[i + 1], s[i]) in babs:
                        ssl = True
                    abas.add((s[i], s[i + 1]))
    if not_tls:
        tls = False
    return tls, ssl

nb_tls, nb_ssl = 0, 0
for line in open('test.in'):
    tls, ssl = is_tls_or_ssl(line.rstrip())
    if tls:
        nb_tls += 1
    if ssl:
        nb_ssl += 1

print(nb_tls, nb_ssl)
