import string

def move_ten(st):
    #print(string.ascii_lowercase[1])
    #print(string.ascii_lowercase.index("b"))

    return "".join([string.ascii_lowercase[(string.ascii_lowercase.index(x) + 10)%26] for x in st])

print(move_ten("testcase"))#, "docdmkco")
print(move_ten("codewars"))#, "mynogkbc")
print(move_ten("exampletesthere"))#, "ohkwzvodocdrobo")
print(move_ten("returnofthespacecamel"))#, "bodebxypdroczkmomkwov") 
print(move_ten("bringonthebootcamp"))#, "lbsxqyxdrolyydmkwz") 
print(move_ten("weneedanofficedog"))#, "goxoonkxyppsmonyq") 