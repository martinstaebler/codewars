# https://www.codewars.com/kata/55e2adece53b4cdcb900006c/train/python
from datetime import timedelta
def race(v1, v2, g):
    if v1 > v2: 
        return None
    else:
        t = 3600 * g / (v2 - v1)
        print(timedelta(seconds=t))
        h = int(t / 3600)
        m = int((t % 3600) / 60)
        s = int((t % 3600) % 60)
        return [h, m, s]








print(race(720, 850, 70))#, [0, 32, 18])
print(race(80, 91, 37))#, [3, 21, 49])
print(race(820, 81, 550))#, None)  