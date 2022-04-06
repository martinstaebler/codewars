import numpy as np

def remov_nb_2(n):
    sequence = np.arange(1, n + 1, 1)
    arr_twins = []
    for num1 in sequence:
        rest1 = sequence[sequence != num1]
        for num2 in rest1:
            rest2 = rest1[rest1 != num2]
            if sum(rest2) == num1 * num2:
                twins = (num1, num2)
                arr_twins.append(twins)

    return arr_twins

def remov_nb_3(n):
    arr_twins = []
    sum_sequence = int(n * (n + 1) / 2)
    for x1 in range(1, n+1):
        for x2 in range(1, n+1):
            if x2 != x1 and x1 * x2 == sum_sequence - x1 - x2:
                twins = (x1, x2)
                arr_twins.append((x1, x2))

    return arr_twins

def remov_nb(n):
    arr_twins = []
    sum_sequence = int(n * (n + 1) / 2)
    for x1 in range(1, n+1):
        rest = sum_sequence - x1
        x2 = int(rest / (x1 + 1))
        print(str(x1) + " " + str(x2))
        if (rest % x1 == x2 or rest % x1 + x1 == x2) and (x1 + 1) * x2 == rest:
            arr_twins.append((x1, x2))

    return arr_twins

print(remov_nb(5)) # should return []
print(remov_nb(26)) # should return [(15, 21), (21, 15)]
print(remov_nb(581)) # should return [(15, 21), (21, 15)]
