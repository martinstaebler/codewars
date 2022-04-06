# https://www.codewars.com/kata/58a5aeb893b79949eb0000f1/train/python

def shared_bits(a, b):
    bits_shared = 0
    biggest_bin = len("{0:b}".format(a)) if len("{0:b}".format(a)) > len("{0:b}".format(b)) else  len("{0:b}".format(b))
    a = (f"%0{biggest_bin}d" % int("{0:b}".format(a)))[::-1]
    b = (f"%0{biggest_bin}d" % int("{0:b}".format(b)))[::-1]

    for i in range(0, biggest_bin): 
        if a[i] == "1" and b[i] == "1":
            bits_shared += 1

    return True if bits_shared >= 2 else False 

def shared_bits_2(a, b):
    return bin(a & b).count('1') > 1

print(shared_bits(1, 2))#, False)
print(shared_bits(16, 8))#, False)
print(shared_bits(1, 1))#, False)
print(shared_bits(2, 3))#, False)
print(shared_bits(7, 10))#, False)
print(shared_bits(43, 77))#, True)
print(shared_bits(7, 15))#, True)
print(shared_bits(23, 7))#, True)