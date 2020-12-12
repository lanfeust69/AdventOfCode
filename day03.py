import sys
sys.stdin = open('test.in')

lines = sys.stdin.readlines()

def count_hits(right, down):
    hit = 0
    row = down
    step = 1
    while row < len(lines):
        if lines[row][step * right % (len(lines[row]) - 1)] == '#':
            hit += 1
        row += down
        step += 1
    return hit

print(count_hits(1, 1) * count_hits(3, 1) * count_hits(5, 1) * count_hits(7, 1) * count_hits(1, 2))
