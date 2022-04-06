from re import search

# [a-zA-Z0-9]{6,}

regex="^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{6,}$"

print(search(regex, 'fjd3IR9' )) # True)
print(search(regex, 'ghdfj32' )) # False)
print(search(regex, 'DSJKHD23' )) # False)
print(search(regex, 'dsF43' )) # False)
print(search(regex, '4fdg5Fj3' )) # True)
print(search(regex, 'DHSJdhjsU' )) # False)
print(search(regex, 'fjd3IR9.;' )) # False)
print(search(regex, 'fjd3  IR9' )) # False)
print(search(regex, 'djI38D55' )) # True)
print(search(regex, 'a2.d412' )) # False)
print(search(regex, 'JHD5FJ53' )) # False)
print(search(regex, '!fdjn345' )) # False)
print(search(regex, 'jfkdfj3j' )) # False)
print(search(regex, '123' )) # False)
print(search(regex, 'abc' )) # False)
print(search(regex, '123abcABC' )) # True)
print(search(regex, 'ABC123abc' )) # True)
print(search(regex, 'Password123' )) # True)