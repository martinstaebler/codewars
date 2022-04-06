import numpy as np

def death_star(week, attack): 
    resources_needed = [100, 75, 50]

    for i in range(0, attack):
        resources_needed = np.subtract(resources_needed, week[i])
    resources_needed = [x if x > 0 else 0 for x in resources_needed]
    if resources_needed[0] > 0 or resources_needed[1] > 0 or resources_needed[2] > 0:
        return 'The station is destroyed! It needed {} iron, {} steel and {} chromium for completion.'.format(resources_needed[0], resources_needed[1], resources_needed[2])
    else:
        return "The station is completed!"

print(death_star([[100,75,49],[20,15,20],[10,15,10],[50,50,20],[20,15,10],[20,15,10],[20,15,10]],1))#, 'The station is destroyed! It needed 0 iron, 0 steel and 1 chromium for completion.')
print(death_star([[20,15,10],[20,15,20],[10,15,10],[50,50,20],[20,15,10],[20,15,10],[20,15,10]],5))#, 'The station is completed!')