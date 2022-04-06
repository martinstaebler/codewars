# https://www.codewars.com/kata/55f3da49e83ca1ddae0000ad/train/python

import math

def tankvol(h, d, vt):
    r = 0.5 * d

    length = vt / (math.pi * r ** 2)
    winkel = math.degrees(2 * math.acos((r - h) / r))
    flaeche_gesamt = (math.pi * r ** 2) * (winkel / 360) 
    gegenkathete = math.sqrt( r ** 2 - (r-h)**2)
    flaeche_dreieck =  (r - h) * gegenkathete
    volumen = (flaeche_gesamt - flaeche_dreieck)*length

    return math.floor(volumen)




print(tankvol(5, 7, 3848))#, 2940)
print(tankvol(2, 7, 3848))#, 907)