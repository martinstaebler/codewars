# https://www.codewars.com/kata/597754ba62f8a19c98000030

def vowel_change(txt, vow):
    return "".join([vow if x in "aeiou" else x for x in txt])

print("ac"*10)


print(vowel_change("hannah hannah bo-bannah banana fanna fo-fannah fee, fy, mo-mannah. hannah!",'i'))#, 'hinnih hinnih bi-binnih binini finni fi-finnih fii, fy, mi-minnih. hinnih!');
print(vowel_change('adira wants to go to the park', 'o'))#, 'odoro wonts to go to tho pork');
