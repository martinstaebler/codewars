def simplify(math_expression):
    numbers_operators = "+-123456789"
    arr_expression = math_expression.replace("-"," -").replace("+"," +").strip().split(" ")
    dict_values = {}
    simplified_expression = ""

    for i in arr_expression:
        amount, variables = "", ""
        for chr in i:
            if chr in numbers_operators:
                amount += chr
            else:
                variables += chr
        if len(amount) < 1 or amount == "+" or amount == "-":
            amount += "1"
        variables_sorted ="".join(sorted([ch for ch in variables]))
        amount = int(amount)
        if variables_sorted in dict_values:
            dict_values[variables_sorted] = amount + dict_values[variables_sorted]
        else:
            dict_values[variables_sorted] = amount
    print(dict_values)

    for key in sorted(sorted(dict_values), key=len):
        if dict_values[key] != 0:
            if dict_values[key] > 0 and len(simplified_expression) != 0:
                simplified_expression += "+"

            if dict_values[key] < -1 or dict_values[key] > 1:
                simplified_expression += str(dict_values[key])
            if dict_values[key] == -1:
                simplified_expression += "-"
            simplified_expression += key

    return simplified_expression
    #return ", ".join([str(d) for d in ts[:-1]]) + (" and " if len(ts) > 1 else "") + ts[-1]
    #return "".join([str(dict_values[key]) + key for key in sorted(sorted(dict_values), key=len) if dict_values[key] != 0])



print(simplify("3x-yx+2xy-x"))
print(simplify("cb+cba"))
print(simplify("2xy-yx"))
print(simplify("-a+5ab+3a-c-2a"))
print(simplify("-abc+3a+2ac"))
print(simplify("y-x"))

"""
When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!

Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the following way ( -> means application of simplify):

    All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:

    "cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"

    All monomials appears in order of increasing number of variables, e.g.:

    "-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

    If two monomials have the same number of variables, they appears in lexicographic order, e.g.:

    "a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

    There is no leading + sign if the first coefficient is positive, e.g.:

    "-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"
"""