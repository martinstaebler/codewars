def dig_pow(n, p):
    sum_of_values = sum([int(item[1]) ** (p + int(item[0])) for item in enumerate(str(n))]) / n
    return int(sum_of_values) if sum_of_values.is_integer() else -1



print(dig_pow(89, 1))
print(dig_pow(46288, 3))

#a = [1, 2, 3, 1, 2, 3]
#print([index for index,value in enumerate(a) if value > 2])

