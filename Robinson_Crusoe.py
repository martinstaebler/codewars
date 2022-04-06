from random import randint
from math import cos, sin, pi, radians

def crusoe(n, d, ang, dist_mult, ang_mult):
    x = 0
    y = 0

    for _ in range(0, n):
        x += d * cos(radians(ang))
        y += d * sin(radians(ang))
        d = d * dist_mult
        ang = ang * ang_mult
        
    return x, y



def assert_fuzzy(n, d, ang, distmult, angmult, expect):
    crusoe(n, d, ang, distmult, angmult)

assert_fuzzy(5, 0.2, 30, 1.02, 1.1, (0.8306737544381833, 0.620694691344071))


#assert_fuzzy(8, 0.22, 3, 1.01, 1.15, (1.814652098870, 0.164646220964))
#assert_fuzzy(29, 0.13, 21, 1.01, 1.09, (0.318341393410, 2.292862212314))
#assert_fuzzy(45, 0.10, 3, 1.01, 1.10, (2.689897523779, 2.477953232467))
#assert_fuzzy(14, 0.22, 20, 1.02, 1.14, (1.774076472485, 2.557008479031))
#assert_fuzzy(42, 0.11, 17, 1.02, 1.09, (0.528555980656, 2.196434600133))