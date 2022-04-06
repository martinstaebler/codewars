# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python

def multiplication_table(size):
    list_multiplication = []

    for i in range(0, size):
        list_zeile = []
        for j in range(0, size):
            list_zeile.append((i+1) * (j+1))
        list_multiplication.append(list_zeile)
    return list_multiplication




print(multiplication_table(3)) #[[1,2,3],[2,4,6],[3,6,9]])