# https://www.codewars.com/kata/5aca48db188ab3558e0030fa/train/python

def calc_type(a, b, res):
    return "addition" if a + b == res else "subtraction" if a - b == res else "division" if a / b == res else "multiplication"


def calc_type_1(a, b, res):
    dict = {a+b:'addition',a-b:'subtraction',a*b:'multiplication',a/b:'division'}
    return dict[res]

print(calc_type(1, 2, 3))#, "addition")
print(calc_type(10, 5, 5))#, "subtraction")
print(calc_type(10, 4, 40))#, "multiplication")
print(calc_type(9, 5, 1.8))#, "division")