def one(function, value=1):
    return function(value)

def nothing(value):
    return value

def times(value):
    return value ** 2

print(one(times))

"""
def two(operand):
def three(operand):
def four(operand):
def five(operand):
def six(operand):
def seven(operand):
def eight(operand):
def nine(operand):

def times():
def plus():
def minus():
def devided_by():
"""


# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3