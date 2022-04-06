# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

def change_chars(character):
    if character == "A":
        return "T"
    elif character == "T":
        return "A"
    elif character == "C":
        return "G"
    elif character == "G":
        return "C"
    else:
         return character

# a, t, c, g
# t, a, g, c

def DNA_strand(dna):
    return "".join([change_chars(x) for x in dna])


print(DNA_strand("AAAA"))#,"TTTT","String AAAA is")
print(DNA_strand("ATTGC"))#,"TAACG","String ATTGC is")
print(DNA_strand("GTAT"))#,"CATA","String GTAT is")

# return dna.translate(string.maketrans("ATCG","TAGC"))
# return ''.join([{'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}[letter] for letter in dna])