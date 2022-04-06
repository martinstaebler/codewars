def sum_pairs_me(list_of_numbers, sum):
    set_of_numbers = set(list_of_numbers)
    array_of_pairs = []
    for x in range(0,len(list_of_numbers)):
        friend = sum - list_of_numbers[x]
        if friend in set_of_numbers:
            try:
                array_of_pairs.append([x, list_of_numbers.index(friend, x+1)])
            except:
                pass

    if len(array_of_pairs) > 0:
        first_pair = sorted(array_of_pairs, key=lambda x : x[1])[0]
        final_numbers = [list_of_numbers[first_pair[0]], list_of_numbers[first_pair[1]]]
        return final_numbers
    else:
        return None

def sum_pairs(nums, sum_value):
    seen = set()
    for num in nums:
        diff = sum_value - num
        if diff in seen:
            return [diff, num]
        seen.add(num)

print(sum_pairs([11, 3, 7, 5], 10))
print(sum_pairs([4, 3, 2, 3, 4], 6))
print(sum_pairs([0, 0, -2, 3], 2))
print(sum_pairs([10, 5, 2, 3, 7, 5], 10))

"""sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
"""