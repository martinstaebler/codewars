# https://www.codewars.com/kata/5f25f475420f1b002412bb1f/train/python

def find_the_number_plate(id):
    customer_id = id 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    tausender =  0
    z_tausender = 0
    h_tausender = 0
    
    for i in range(0, int(customer_id/999)):

        customer_id -= 999
        if tausender < 25:
            tausender += 1
        else:
            tausender = 0

            if z_tausender < 25:
                z_tausender += 1
            else:
                h_tausender += 1
                z_tausender = 0
                tausender = 0
     
    return "{}{}{}{:03}".format(alphabet[tausender], alphabet[z_tausender], alphabet[h_tausender], customer_id+ 1)
   
    #return 
 
def find_the_number_plate_2(id):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    hunderter = id % 999 + 1
    h_tausender = id//(999*26*26)    
    z_tausender = (id % (999*26*26)) // (999*26)
    tausender = (id % (999*26)) // 999

    return "{}{}{}{:03}".format(alphabet[tausender], alphabet[z_tausender], alphabet[h_tausender], hunderter)


print(find_the_number_plate_2(3))
print(find_the_number_plate_2(1487))
print(find_the_number_plate_2(40000))


"""
find_the_number_plate_2(1487) #'baa489'),
find_the_number_plate(234567) #aja802'),
find_the_number_plate(17558423) #'zzz999'),
find_the_number_plate_2(17558423) #'zzz999'),

find_the_number_plate(3) #'aaa004'),
find_the_number_plate(1000) #'aaa004'),
find_the_number_plate(100000) #'aaa004'),
find_the_number_plate(1487) #'baa489'),
find_the_number_plate(40000) #'oba041'),
find_the_number_plate(17558423) #'zzz999'),
find_the_number_plate(234567) #aja802'),"""