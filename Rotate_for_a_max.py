# https://www.codewars.com/kata/56a4872cbb65f3a610000026/train/python

def max_rot(n):
    max = n
    n_str = str(n)
    
    for i in range(0, len(n_str)):
        n_str = n_str[0:i] + n_str[i+1:] + n_str[i]
        print(n_str)
        if int(n_str) > max:
            max = int(n_str)
            
    return max



#print(max_rot(38458215))#, 85821534)
#print(max_rot(195881031))#, 988103115)
#print(max_rot(896219342))#, 962193428)
print(max_rot(97552397732612))#,75523977326129 )
