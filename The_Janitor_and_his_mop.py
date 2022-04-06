# https://www.codewars.com/kata/59128363e5bc24091a00006f
import numpy as np
def the_janitor(word):
    all_chars = sorted(list(set(word)))
    
    return_list = np.zeros(26, dtype=int)
    for character in all_chars:
        return_list[ord(character) - 97] = word.rindex(character) - word.index(character) + 1 
    return(list(return_list))
        


print(the_janitor("abacaba"))#, [7, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(the_janitor("likemm"))#, [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(the_janitor("rkuhsxtflzvytbtwxyarsglibmhfmmikyolfmopbtkzxezjahq"))#, [30, 27, 0, 0, 1, 29, 1, 46, 8, 1, 41, 27, 12, 0, 5, 1, 1, 20, 17, 35, 1, 1, 1, 39, 22, 37])
print(the_janitor("ommnommnomm"))#, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 5, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])