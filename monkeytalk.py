# https://www.codewars.com/kata/59f897ecc374cb9ed90000c2/train/python

def monkey_talk(phrase):
    sentence = phrase.split(" ")
    translation = [x[-1]+x[-1] + "k" for x in sentence]
    translation = " ".join(translation) + "."
    return translation[0].upper() + translation[1:]



monkey_talk('Hello') # , 'Ook.')
monkey_talk('Everyone') # , 'Eek.')
monkey_talk('Hello Everyone') # , 'Ook eek.')
monkey_talk('Everyone Hello') # , 'Eek ook.')