# https://www.codewars.com/kata/5574835e3e404a0bed00001b/train/python

import math

def get_participants(handshakes):
    i = 1
    while math.comb(i, 2) < handshakes:
        i += 1
    return i
    





print(get_participants(0))# 1)
print(get_participants(1))# 2)
print(get_participants(3))# 3)
print(get_participants(6))# 4)
print(get_participants(7))# 5)
