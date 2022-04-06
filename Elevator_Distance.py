# https://www.codewars.com/kata/59f061773e532d0c87000d16/train/python

def elevator_distance(array):
    return sum([abs(j-i) for i, j in zip(array[:-1], array[1:])])

# t = [1, 3, 6]
# v = [t[i+1]-t[i] for i in range(len(t)-1)]
# v

print(elevator_distance([5,2,8]))#, 9)
print(elevator_distance([1,2,3]))#, 2)
print(elevator_distance([7,1,7,1]))#, 18)