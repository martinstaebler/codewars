# https://www.codewars.com/kata/5551dc71101b2cf599000023/train/python

def max_pizza(cuts):
    return -1 if cuts < 0 else cuts * (cuts + 1)/2 + 1

#N = letztes Element
#Summe = N * ( N + 1 ) / 2 

print(max_pizza(-2))#, -1)
print(max_pizza(0))#, 1)
print(max_pizza(3))#, 7)
print(max_pizza(4))#, 11)
print(max_pizza(5))#, 16)
print(max_pizza(6))#, 22)