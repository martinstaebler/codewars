def rot13(message):
    shifted_string = [shift_character(ch) for ch in message]
    return shifted_string

def shift_character(ch):
    ch_num = ord(ch)
    if ch_num >= 65 and ch_num <= 90:
        ch_num += 13
        if ch_num > 90:
            ch_num += -26
    elif ch_num >= 97 and ch_num <= 122:
        ch_num += 13
        if ch_num > 122:
            ch_num += -26
    return chr(ch_num)

print(rot13("az")) #"grfg"
print(rot13("AZ")) #"grfg"
print(rot13("test")) #"grfg"
print(rot13("Test")) #"Grfg"

def rot13_1(message):
    return ''.join(chr((65 if c.isupper() else 97) + ((ord(c) - (65 if c.isupper() else 97)) + 13)%26) if c.isalpha() else c for c in message)


import string
from codecs import encode as _dont_use_this_
from string import maketrans, lowercase, uppercase

def rot13_2(message):
    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
    return message.translate(lower).translate(upper)