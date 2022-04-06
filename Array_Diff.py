def array_diff(list_1, list_2):
    return [item for item in list_1 if item not in list_2]

print(array_diff([1,2],[1]))
print(array_diff([1,2,2,2,3],[2]))