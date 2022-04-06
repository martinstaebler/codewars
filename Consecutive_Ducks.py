# https://www.codewars.com/kata/5dae2599a8f7d90025d2f15f

def consecutive_ducks(n):

    if n % 2 != 0:
        return True
    else:
        for i in range(2, n//2):
            differenz = (i-1)*i / 2
            if (n - differenz)%i == 0 and n - differenz > 0:
                return True
            
    
    return False
    
print(consecutive_ducks(323744))# True)   
"""
print(consecutive_ducks(69))# True)
print(consecutive_ducks(8))# False)
print(consecutive_ducks(57))# True)
print(consecutive_ducks(6))# True)
print(consecutive_ducks(13))# True)
print(consecutive_ducks(16))# False)
print(consecutive_ducks(91))# True)
print(consecutive_ducks(75))# True)
print(consecutive_ducks(38))# True)
print(consecutive_ducks(25))# True)
print(consecutive_ducks(32))# False)
print(consecutive_ducks(65))# True)
print(consecutive_ducks(13))# True)
print(consecutive_ducks(16))# False)
print(consecutive_ducks(99))# True)

print(consecutive_ducks(522))# True)
print(consecutive_ducks(974))# True)
print(consecutive_ducks(755))# True)
print(consecutive_ducks(512))# False)
print(consecutive_ducks(739))# True)
print(consecutive_ducks(1006))# True)
print(consecutive_ducks(838))# True)
print(consecutive_ducks(1092))# True)
print(consecutive_ducks(727))# True)
print(consecutive_ducks(648))# True)
print(consecutive_ducks(1024))# False)
print(consecutive_ducks(851))# True)
print(consecutive_ducks(541))# True)
print(consecutive_ducks(1011))# True)
print(consecutive_ducks(822))# True)

print(consecutive_ducks(382131))# True)
print(consecutive_ducks(118070))# True)
print(consecutive_ducks(17209))# True)
print(consecutive_ducks(32768))# False)
print(consecutive_ducks(161997))# True)
print(consecutive_ducks(400779))# True)
print(consecutive_ducks(198331))# True)
print(consecutive_ducks(325482))# True)
print(consecutive_ducks(88441))# True)
print(consecutive_ducks(648))# True)
print(consecutive_ducks(65536))# False)

print(consecutive_ducks(183540))# True)
print(consecutive_ducks(65271))# True)
print(consecutive_ducks(5263987))# True)
"""