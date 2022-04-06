# https://www.codewars.com/kata/584d88622609c8bda30000cf/train/python

def word_splitter_2(string1):
    
    dict_special = {}
    highest_key = ""
    for character in string1:
        if not character.isalnum():
            if character in dict_special:
                dict_special[character] = dict_special[character] + 1
            else:
                dict_special[character] = 1
    highest_key = list(dict_special.keys())[0] 
    for key in dict_special:
        if dict_special[highest_key] < dict_special[key]:
            highest_key = key
    return string1.split(highest_key)

def word_splitter(string1):
    return "".join(["@" if x in ":;!@#$%^&*()?_=,<>/|+" else x for x in string1]).split("@")

print(word_splitter("12:56C:144:1000:1200"))
#test.assert_equals(example1, ["12","56C","144","1000","1200"])
print(word_splitter("23;RPM;300;PSI;MODE;FORWARD"))
#test.assert_equals(example2, ["23","RPM","300","PSI","MODE","FORWARD"])


print(word_splitter("340000.00*-140.49902*ELEVATION*24000000*END"))
#test.assert_equals(example3, ["340000.00","-140.49902","ELEVATION","24000000","END"])