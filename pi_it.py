import string

def pig_it(sentence):
    return " ".join([word[1:] + word[0] + "ay" if word not in set(string.punctuation) else word for word in sentence.split()])
    #return " ".join([word[0] + "lay" for word in sentence.split() if len(word) > 1])

print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
print(pig_it('Hello world !'))     # elloHay orldway !