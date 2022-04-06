#https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

def longest(a1, a2):
    
    return "".join(sorted(list(set([x for x in a1+a2]))))



print(longest("aretheyhere", "yestheyarehere"))#, "aehrsty")
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))#, "abcdefghilnoprstu")
print(longest("inmanylanguages", "theresapairoffunctions"))#, "acefghilmnoprstuy")
