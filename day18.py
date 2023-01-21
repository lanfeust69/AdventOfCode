first = [c == '.' for c in '.^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^.']
n = len(first)

safe = set([(False, False, False), (False, True, False), (True, False, True), (True, True, True)])
current = first
total_safe = 0
for _ in range(400000):
    total_safe += sum(current)
    current = [(True, current[0], current[1]) in safe] + [(current[i - 1], current[i], current[i + 1]) in safe for i in range(1, n - 1)] + [(current[-2], current[-1], True) in safe]

print(total_safe)
