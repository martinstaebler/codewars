# https://www.codewars.com/kata/52724507b149fa120600031d

def number2words(number_int):
    dict_numbers = {1: "one",
                    2: "two",
                    3: "three",
                    4: "four",
                    5: "five",
                    6: "six",
                    7: "seven",
                    8: "eight",
                    9: "nine",
                    10: "ten",
                    11: "eleven",
                    12: "twelve",
                    13: "thirteen",
                    14: "fourteen",
                    15: "fifteen",
                    16: "sixteen",
                    17: "seventeen",
                    18: "eighteen",
                    19: "nineteen",
                    20: "twenty",
                    30: "thirty",
                    40: "forty",
                    50: "fifty",
                    60: "sixty",
                    70: "seventy",
                    80: "eighty",
                    90: "ninety"}

    if number_int == 0:
        return "zero"
    else:
        words_thousand = ""
        words_number = ""
        
        tens = '{:06d}'.format(number_int)[4:6]
        hundreds = '{:06d}'.format(number_int)[3:4]
        thousands = '{:06d}'.format(number_int)[1:3]
        h_thousands = '{:06d}'.format(number_int)[0]

        try:
            words_thousand = dict_numbers[int(h_thousands)] + " hundred "
        except:
            pass

        try:
            words_thousand += dict_numbers[int(thousands)] + " "
        except:
            try:
                 words_thousand += "{}-{} ".format(dict_numbers[int(thousands[0]+"0")], dict_numbers[int(thousands[1])])
            except:
                pass

        if len(words_thousand) > 0:
            words_number = words_thousand + "thousand "

        try:
            words_number += dict_numbers[int(hundreds)] + " hundred "
        except:
            pass

        try:
            words_number += dict_numbers[int(tens)]
        except:
            try:
                 words_number += "{}-{}".format(dict_numbers[int(tens[0]+"0")], dict_numbers[int(tens[1])])
            except:
                pass

        return words_number.strip()




words = "zero one two three four five six seven eight nine" + \
" ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty" + \
" thirty forty fifty sixty seventy eighty ninety"
words = words.split(" ")

def number2words_2(n):
    if n < 20:
        return words[n]
    elif n < 100:
        return words[18 + n // 10] + ('' if n % 10 == 0 else '-' + words[n % 10])
    elif n < 1000:
        return number2words(n // 100) + " hundred" + (' ' + number2words(n % 100) if n % 100 > 0 else '')
    elif n < 1000000:
        return number2words(n // 1000) + " thousand" + (' ' + number2words(n % 1000) if n % 1000 > 0 else '')

number2words(0)
number2words(888888)
number2words(88)
number2words(88)
number2words(17)
number2words(11)


number2words(0)  #  "zero"
number2words(1)  #  "one"
number2words(9)  #  "nine"
number2words(10)  #  "ten"
number2words(17)  #  "seventeen"
number2words(20)  #  "twenty"
number2words(21)  #  "twenty-one"
number2words(45)  #  "forty-five"
number2words(80)  #  "eighty"
number2words(99)  #  "ninety-nine"
number2words(100)  #  "one hundred"
number2words(301)  #  "three hundred one"
number2words(799)  #  "seven hundred ninety-nine"
number2words(800)  #  "eight hundred"
number2words(950)  #  "nine hundred fifty"
number2words(1000)  #  "one thousand"
number2words(1002)  #  "one thousand two"
number2words(3051)  #  "three thousand fifty-one"
number2words(7200)  #  "seven thousand two hundred"
number2words(7219)  #  "seven thousand two hundred nineteen"
number2words(8330)  #  "eight thousand three hundred thirty"
number2words(99999)  #  "ninety-nine thousand nine hundred ninety-nine"
print(number2words(888888))  #  "eight hundred eighty-eight thousand eight hundred eighty-eight"
