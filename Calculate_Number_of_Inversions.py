# https://www.codewars.com/kata/537529f42993de0e0b00181f

def count_inversions(array):
    inversions = 0
    sorted_arr = "".join(str(e) for e in sorted(array))
    
    while sorted_arr != "".join(str(e) for e in array):
        for index in range(0, len(array)-1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                inversions += 1
    return inversions

print(count_inversions([]))#, 0)
print(count_inversions([1,2,3]))#, 0)
print(count_inversions([2,1,3]))#, 1)
print(count_inversions([6,5,4,3,2,1]))#, 15)
print(count_inversions([6,5,4,3,3,3,3,2,1]))#, 30)