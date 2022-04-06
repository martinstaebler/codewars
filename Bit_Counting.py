# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

def count_bits(n):
    return format(n, "b").count("1")



print(count_bits(0))#, 0)
print(count_bits(4))#, 1)
print(count_bits(7))#, 3)
print(count_bits(9))#, 2)
print(count_bits(10)) #, 2)