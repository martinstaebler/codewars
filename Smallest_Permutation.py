# https://www.codewars.com/kata/5fefee21b64cc2000dbfa875

def min_permutation(n):
    sorted_array = sorted([int(x) for x in str(abs(n))])
    for number in range(0, len(sorted_array)):
        if sorted_array[number] > 0:
           sorted_array.insert(0, sorted_array.pop(number))
           break
    sorted_number = "".join([ str(x) for x in sorted_array])
    return int("-" + sorted_number) if n < 0 else int(sorted_number)



print(min_permutation(-20))#, -20)
min_permutation(-32)#, -23)
min_permutation(0)#, 0)
min_permutation(10)#, 10)
print(min_permutation(2903094))#, 23499)