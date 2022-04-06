# https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/train/python

import numpy

def gap_2(g, m, n):

    primes = list()

    for i in range(m, n+1): 
        if i%2 == 1 and i%3 != 0 and i%5 != 0 and i%7 != 0:
            divisors = numpy.arange(3, int(i/3)+1)
            is_prime = True
            for d in divisors:
                if i%d == 0:
                    is_prime = False
                    break
            if is_prime == True:
                primes.append(i)    
                if len(primes) > 1:
                    if primes[-1] - primes[-2] == g:
                        return list([primes[-2],primes[-1]])
                        break
    return None

def gap(g, m, n):

    prev_prime = 0
    curr_prime = 0

    for i in range(m, n+1): 
        if i%2 == 1 and i%3 != 0 and i%5 != 0 and i%7 != 0:
            divisors = numpy.arange(3, int(i/3)+1)
            is_prime = True
            for d in divisors:
                if i%d == 0:
                    is_prime = False
                    break
            if is_prime == True:
                curr_prime = i    
                if prev_prime != 0:
                    if curr_prime - prev_prime == g:
                        return curr_prime
                        break
                prev_prime = curr_prime
    return None

 
import math
import numpy
def prime5(upto=1000):
    primes=numpy.arange(2,upto+1)
    isprime=numpy.ones(upto-1,dtype=bool)
    for factor in primes[:int(math.sqrt(upto))]:
        print(factor)
        if isprime[factor-2]: isprime[factor*2-2::factor]=0
    return primes[isprime]


print(gap(2,100,110)) # [101, 103])
print(gap(4,100,110)) # [103, 107])
print(gap(6,100,110)) # None)
print(gap(8,300,400)) # [359, 367])
print(gap(10,300,400)) # [337, 347])

#print(prime5())