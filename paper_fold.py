# https://www.codewars.com/kata/5d26721d48430e0016914faa/train/python


def o_or_z(i_number):
    return "0" if i_number == 0 else str(i_number%2)

def paper_fold():

    n_string = "1"
    while len(n_string) <= 1000000:
        n_string = "1" + "".join([x + o_or_z(ind) for ind, x in enumerate(n_string)])
    return iter([int(x) for x in n_string])

print(paper_fold())

# https://www.w3schools.com/python/python_iterators.asp

