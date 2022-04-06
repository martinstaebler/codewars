# https://www.codewars.com/kata/61707b71059070003793bc0f/train/python

def find_height(cubes):
    num_layer, amount_groundlayer, sum_elements = 0, 0, 0

    while sum_elements <= cubes:
        num_layer += 1
        amount_groundlayer += num_layer
        sum_elements += amount_groundlayer
     
    find_height=lambda x:(n:=int((6*x)**(1/3)))-(n*(n+1)*(n+2)>6*x)

    return num_layer - 1



print(find_height(0))#, 0)
print(find_height(1))#, 1)
print(find_height(3))#, 1)
print(find_height(4))#, 2)
print(find_height(10))#, 3)