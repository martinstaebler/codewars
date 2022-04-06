# https://www.codewars.com/kata/56d8f14cba01a83cdb0002a2/train/python

def get_positions(n):
    return n%3, n//3%3, n//9%3






print(get_positions(54)) #, (0, 0, 0))
print(get_positions(98)) #, (2, 2, 1))
print(get_positions(3)) #, (0, 1, 0))