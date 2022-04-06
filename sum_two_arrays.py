# https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6/train/python

def sum_arrays_2(array1,array2):
    if not array1: return array2
    if not array2: return array1
    num = sum(map(lambda x: int(''.join(map(str, x))), [array1, array2]))
    lst = list(map(int, str(abs(num))))
    if num < 0: lst[0] *=-1
    return lst
import re

def sum_arrays(array1, array2):
    # if len(array1) == 0 and len(array2) == 0:
    #    return [] 

    """ 
    number_1 = int(''.join(str(e) for e in array1)) if len(array1) > 0 else 0
    number_2 = int(''.join(str(e) for e in array2)) if len(array2) > 0 else 0
    result = str(number_1 + number_2)
    """
    
    # Lines above in one line
    result = str((int(''.join(str(e) for e in array1)) if len(array1) > 0 else 0) + ((int(''.join(str(e) for e in array2)) if len(array2) > 0 else 0)))
    regex = r"-\d(?=\d)"

    return [] if (len(array1) == 0 and len(array2) == 0) else [int(re.findall(regex, result)[0])] + [int(x) for x in result.replace(re.findall(regex, result)[0], "")] if (int(result) < 0 and len(result) > 2)  else [int(result)] if int(result) < 0 else [int(x) for x in result]



print(sum_arrays([3,2,6,6],[-7,2,2,8]))#[-3, 9, 6, 2]
print(sum_arrays([3,2,9],[1,2]))#,[3,4,1])
print(sum_arrays([4,7,3],[1,2,3]))#,[5,9,6])
print(sum_arrays([1],[5,7,6]))#,[5,7,7])
print(sum_arrays([-3,4,2],[3,4,4]))#,[2])
print(sum_arrays([],[]))#,[])
print(sum_arrays([0],[]))#,[0])
print(sum_arrays([],[1,2]))#,[1,2])
print(sum_arrays([-1],[0]))#,[1,2])



