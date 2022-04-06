# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
    errors = 0
    for i in s:
        if (ord(i) - 97) > (ord("m") - 97):
            errors += 1

    return str(errors) + "/" + str(len(s))

def printer_error_2(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s))#, "3/56")
t = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(t))#, "6/60")
u = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
print(printer_error(u))# , "11/65")