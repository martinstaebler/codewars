def likes(names_list):
    len_list = len(names_list)
    return "{}, {} and {length} more like this".format(*names_list, length=len_list-2) if len_list > 3 else "{}, {} and {} like this".format(*names_list) if len_list == 3 else "{} and {} like this".format(*names_list) if len_list == 2 else "{} likes this".format(*names_list) if len_list > 0 else "no one likes this"


print(likes([]))  # must be "no one likes this"
print(likes(["Peter"]))  # must be "Peter likes this"
print(likes(["Jacob", "Alex"]))  # must be "Jacob and Alex like this"
print(likes(["Max", "John", "Mark"]))  # must be "Max, John and Mark like this"
print(likes(["Alex", "Jacob", "Mark", "Max"]))  # must be "Alex, Jacob and 2 others like this"