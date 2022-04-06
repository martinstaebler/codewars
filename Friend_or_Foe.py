def friend_or_foe(list):
    return [name for name in list if len(name) == 4]

print(friend_or_foe(["Ryan", "Kieran", "Mark"]))