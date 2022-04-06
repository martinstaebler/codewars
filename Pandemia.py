# https://www.codewars.com/kata/5e2596a9ad937f002e510435

def infected(s):
    return 0 if len(s.replace("X","")) == 0 else len("".join([x for x in list(filter(None,s.split("X"))) if int(x) > 0])) / len(s.replace("X","")) * 100



print(infected("01000000X000X011X0X"))#,73.33333333333333),
print(infected("01X000X010X011XX"))#, 72.72727272727273),
print(infected("XXXXX"))#, 0),
print(infected("00000000X00X0000"))#, 0),
print(infected("0000000010"))#, 100),
print(infected("000001XXXX0010X1X00010"))#, 100),
print(infected("X00X000000X10X0100"))#,42.857142857142854),