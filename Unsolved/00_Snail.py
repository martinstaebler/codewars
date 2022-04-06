# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

import numpy as np
import copy

def snail(snail_map):
    padding = 1
    arr_snail = np.array(snail_map)
    arr_result = []

    while len(arr_snail) > 0:
        if len(arr_snail) > 1:
            arr_result += np.ndarray.flatten(arr_snail[0:1,0:-1]).tolist() + np.ndarray.flatten(arr_snail[0:-1,-1]).tolist() + np.ndarray.flatten(arr_snail[-1,1:])[::-1].tolist() + np.ndarray.flatten(arr_snail[1:,0])[::-1].tolist()
        else:
            arr_result += arr_snail[0].tolist()
        arr_copy = copy.deepcopy(arr_snail[padding:-1*padding,padding:-1*padding])
        arr_snail = copy.deepcopy(arr_copy)

    return arr_result


snail([[1,2,3],  [4,5,6],  [7,8,9]])#[1,2,3,6,9,8,7,4,5]
#snail([[1,2,3], [8,9,4], [7,6,5]])#[1,2,3,4,5,6,7,8,9]
snail([[1,2,3,4],  [5,6,7,8],  [9,10,11,12], [13,14,15,16]])
snail([[1,2,3,4,5],  [6,7,8,9,10],  [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]])
