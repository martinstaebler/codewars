# https://www.codewars.com/kata/5592e3bd57b64d00f3000047

def find_nb(m):
    volume = 0
    layer = 0

    while volume < m:
        layer += 1
        volume += layer ** 3
    return layer if volume == m else -1


print(find_nb(4183059834009))#, 2022)
print(find_nb(24723578342962))#, -1)
print(find_nb(135440716410000))#, 4824)
print(find_nb(40539911473216))#, 3568)
print(find_nb(26825883955641))#, 3218)
