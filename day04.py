import sys, re
sys.stdin = open('test.in')

def check_year(y, inf, sup):
    if not re.match(r'\d{4}$', y):
        return False
    yy = int(y)
    return inf <= yy <= sup

def check_height(v):
    m = re.match(r'(\d+)(in|cm)$', v)
    if not m:
        return False
    h = int(m.group(1))
    if m.group(2) == 'in':
        return 59 <= h <= 76
    else:
        return 150 <= h <= 193

eye_colors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

required = {
    'byr': lambda v: check_year(v, 1920, 2002),
    'iyr': lambda v: check_year(v, 2010, 2020),
    'eyr': lambda v: check_year(v, 2020, 2030),
    'hgt': check_height,
    'hcl': lambda v: re.match(r'#[0-9a-f]{6}$', v),
    'ecl': lambda v: v in eye_colors,
    'pid': lambda v: re.match(r'\d{9}$', v)
}

def check_all(d):
    for f, v in required.items():
        if f not in d or not v(d[f]):
            return False
    return True

current = {}
nb_ok = 0
for line in sys.stdin:
    if line == '\n':
        if check_all(current):
            nb_ok += 1
        current = {}
        continue
    line = line[:-1]  # strip '\n'
    for f in line.split():
        current[f.split(':')[0]] = f.split(':')[1]

if check_all(current):
    nb_ok += 1

print(nb_ok)
