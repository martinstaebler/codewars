# https://www.codewars.com/kata/586bca7fa44cfc833e00005c/train/python

def create_array_of_tiers(n):
    # your awesome code here
    result = []
    for i in range(1, len(str(n)) + 1):
        result.append(str(n)[:i])    
    return result






print(create_array_of_tiers(420))# ["4", "42", "420"])
print(create_array_of_tiers(2017))# ["2", "20", "201", "2017"])
print(create_array_of_tiers(2010))# ["2", "20", "201", "2010"])
print(create_array_of_tiers(2017))# ["2", "20", "201", "2017"])
print(create_array_of_tiers(4020))# ["4", "40", "402", "4020"])
print(create_array_of_tiers(2017))# ["2", "20", "201", "2017"])
print(create_array_of_tiers(80200))# ["8", "80", "802", "8020", "80200"])