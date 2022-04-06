def stock_list(listOfArt, listOfCat):
    cat_numbers = {}
    sum_books = 0
    for cat in listOfCat:
        cat_numbers[cat] = 0
        for book in listOfArt:
            arr_book = book.split(" ")
            if str(arr_book[0])[0] == cat:
                cat_numbers[cat] = cat_numbers.get(cat) + int(arr_book[1])
                sum_books += int(arr_book[1])

    return " - ".join(["(" + key + " : " + str(cat_numbers[key]) + ")" for key in cat_numbers]) if sum_books > 0 else ""


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]



print(stock_list(b, c)) # "(A : 200) - (B : 1140)")