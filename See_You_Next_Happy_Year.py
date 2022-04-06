# https://www.codewars.com/kata/5ae7e3f068e6445bc8000046/train/python

def next_happy_year(year):
    year += 1

    while len(set(str(year))) != 4:
        year += 1

    return year
    #your code here


print(next_happy_year(1001)) #,1023)
print(next_happy_year(1123)) #,1203)
print(next_happy_year(2001)) #,2013)
print(next_happy_year(2334)) #,2340)
print(next_happy_year(3331)) #,3401)
print(next_happy_year(1987)) #,2013)
print(next_happy_year(5555)) #,5601)
print(next_happy_year(7712)) #,7801)
print(next_happy_year(8088)) #,8091)
print(next_happy_year(8999)) #,9012)
