# https://www.codewars.com/kata/589896b99c70093f3e00005b/train/python

import math 

def sixteen_circles_2(r):
    dist_x1 = math.sqrt((2*r)**2 - r**2)
    dist_x2 = math.sqrt((2*r)**2 / 2)
    dist_x3 = r

    return round(dist_x1 + dist_x2 - 2 * dist_x3, 2)

def sixteen_circles(r):
    return round(math.sqrt((2*r)**2 - r**2) + math.sqrt((2*r)**2 / 2) - 2 * r, 2)

print(sixteen_circles(3))#, 3.44)
print(sixteen_circles(15))#, 17.19)
