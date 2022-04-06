def create_phone_number(phone_number):
    ph_number = "".join([str(item) for item in phone_number])
    return "(" + ph_number[0:3] + ") " + ph_number[3:6] + "-" + ph_number[6:]

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

print("{}{}".format(*[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print("{}".format(*[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))