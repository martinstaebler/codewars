# https://www.codewars.com/kata/54d496788776e49e6b00052f

def sum_for_list(lst):
    print(lst[len(lst)-1])
    for i in range(0, lst[len(lst)-1]+1):
        for j in range(2, i):
            if i%j != 0:
                print(j)

    return ""

a = [12, 15]
print(sum_for_list(a))#, [[2, 12], [3, 27], [5, 15]])

a = [15, 21, 24, 30, 45]
#print(sum_for_list(a))#, [[2, 54], [3, 135], [5, 90], [7, 21]])