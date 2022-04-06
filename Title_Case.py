# https://www.codewars.com/kata/5202ef17a402dd033c000009

def title_case(input_string, words=""):
    list_words = [x.lower() for x in words.split(" ")]
    if len(input_string) > 0:
        output_string = " ".join([x.lower() if x.lower() in list_words else x.capitalize() for x in input_string.split(" ")])
        print(output_string[0].upper() + output_string[1:])
    else:
        return ''




title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
title_case('First a of in', 'an often into') # 'First A Of In'