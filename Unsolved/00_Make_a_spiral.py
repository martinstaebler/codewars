# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python

import numpy as np

def spiralize(size):
    borders = [0, size - 1, size - 1, 0] #top | right | bottom | left
    spiral = np.zeros((size, size), dtype=int).tolist()


    # move right

    # move down

    # move left

    # move up
    borders[0] += 2

    return spiral, borders


print(spiralize(5))