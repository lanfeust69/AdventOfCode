import math

times = [7, 15, 30]
dists = [9, 40, 200]
times = [71530]
dists = [940200]
times = [61, 67, 75, 71]
dists = [430, 1036, 1307, 1150]
times = [61677571]
dists = [430103613071150]
res = 1
for time, dist in zip(times, dists):
    # t**2 - time * t + dist < 0
    delta = time**2 - 4 * dist
    t0 = int((time - math.sqrt(delta)) / 2)
    while t0 * (time - t0) > dist:
        t0 -= 1
    while t0 * (time - t0) <= dist:
        t0 += 1
    t1 = int((time + math.sqrt(delta)) / 2)
    while t1 * (time - t1) > dist:
        t1 += 1
    while t1 * (time - t1) <= dist:
        t1 -= 1
    res *= t1 - t0 + 1

print(res)
