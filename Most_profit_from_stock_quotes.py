# https://www.codewars.com/kata/597ef546ee48603f7a000057/train/python

def get_most_profit_from_stock_quotes(quotes): 
    profit = 0
    while len(quotes) >= 2:
        profit +=  max(quotes) * (quotes.index(max(quotes)))- sum(quotes[0:quotes.index(max(quotes))])
        quotes = quotes[quotes.index(max(quotes))+1:]
    return profit

#print(get_most_profit_from_stock_quotes([1, 2, 3, 4, 5, 6]))#, 15)
#print(get_most_profit_from_stock_quotes([6, 5, 4, 3, 2, 1]))#, 0)
#print(get_most_profit_from_stock_quotes([1, 6, 5, 10, 8, 7]))#, 18)
print(get_most_profit_from_stock_quotes([1, 6, 5, 10, 8, 9, 8, 7, 6, 5]))#, 19)
#print(get_most_profit_from_stock_quotes([4897, 6992, 2903, 6371, 9440, 8615, 8744, 2576, 3935, 5262, 433, 3331, 3372, 8327, 8186, 5688, 4701, 9476, 5562, 2836, 5865, 241, 6755, 4976, 7684, 6843, 1469, 8302, 318, 5604, 6179, 385, 8887, 9875, 7932, 5528, 5149, 6317, 5496, 2155, 6748, 7839, 5991, 3526, 2685, 2485, 2250, 2717, 7401, 1609, 6756, 9477, 2973, 6893, 6354, 1439, 1762, 8978, 7474, 5366, 1481, 3853, 2887, 8615, 5094, 38, 7307, 4391, 2825, 6719, 3426, 7954, 4361, 6097, 5781, 4184, 4230]))#, 18)