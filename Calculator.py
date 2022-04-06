def calculator(operation):
    arr_operation = [x for x in operation if x != " "]
    arr_calculated = []
    print(arr_operation)
    while len(arr_operation) > 0:
        if "/" in arr_operation:
            pass

    return operation[0]

calculator("2 / 2 + 3 * 4 - 6")
calculator("( 2 + 2 ) * 4")