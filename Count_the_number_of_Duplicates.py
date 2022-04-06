# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

import collections
def duplicate_count(text):
    return len([x for x in collections.Counter(text.lower()).values() if x > 1])
     

print(duplicate_count(""))#, 0)
print(duplicate_count("abcde"))#, 0)
print(duplicate_count("abcdeaa"))#, 1)
print(duplicate_count("abcdeaB"))#, 2)
print(duplicate_count("Indivisibilities")) #, 2)