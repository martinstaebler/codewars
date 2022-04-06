# https://www.codewars.com/kata/57faa6ff9610ce181b000028/train/python
import numpy as np

def crap(garden, bags, cap):
    capacity = bags * cap
    one_d_array = "".join(np.array(garden).flatten())
    if "D" in one_d_array:
        return "Dog!!"
    elif capacity - one_d_array.count("@") >= 0:
        return "Clean"
    else:
        return "Cr@p"


print(crap([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']], 2, 2))#, "Clean")
print(crap([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']], 1, 1))#, "Cr@p")
print(crap([['_','_'], ['_','@'], ['D','_']], 2, 2))#, "Dog!!")
print(crap([['_','_','_','_'], ['_','_','_','_'], ['_','_','_', '_']], 2, 2))#, "Clean")
print(crap([['@','@'], ['@','@'], ['@','@']], 3, 2))#, "Clean")