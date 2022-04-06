# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    list_sentence = " ".join([x[::-1] if len(x) > 5 else x for x in sentence.split(" ")])
    print(list_sentence)
    return None



spin_words( "Hey fellow warriors" )# => returns "Hey wollef sroirraw"

spin_words( "This is a test")# => returns "This is a test"

spin_words( "This is another test" )#=> returns "This is rehtona test"