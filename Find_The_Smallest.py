# https://www.codewars.com/kata/573992c724fc289553000e95/train/python
import copy

def smallest(old_number):
    digits = [int(x) for x in str(old_number)]

    alltime_low = old_number
    last_i = 9999
    last_j = 0
    for i in range(0, len(digits)):
        for j in range(0, len(digits)):
            digits_copy = copy.deepcopy(digits)
            digits_copy.insert(j, digits_copy.pop(i))
            if alltime_low >= int("".join(str(x) for x in digits_copy)):
                if alltime_low == int("".join(str(x) for x in digits_copy)):
                    if i < last_i:
                        last_i = i
                        last_j = j
                else:
                    last_i = i
                    last_j = j

                alltime_low = int("".join(str(x) for x in digits_copy))

                

            
            
    print(digits_copy, alltime_low, last_i, last_j)
    return [alltime_low, last_i, last_j]



smallest(261235)# [126235, 2, 0]);
smallest(209917)# [29917, 1, 0]);
smallest(285365)# [238565, 3, 1]);
smallest(269045)# [26945, 3, 0]);
smallest(296837)# [239687, 4, 1]);
smallest(1000000) #--> [1, 0, 6] 