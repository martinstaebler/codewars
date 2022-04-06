import math

def persistence(input_number):
    num_loops = 0
    product_of_digits = input_number
    #print(math.prod([int(i) for i in str(product_of_digits)]))
    while product_of_digits >= 10:
        product_of_digits = math.prod([int(i) for i in str(product_of_digits)])
        num_loops += 1

    return num_loops

print(persistence(39))
print(persistence(999))
print(persistence(4))
