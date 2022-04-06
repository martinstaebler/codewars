def decode(string):
    #your code here    
    return "".join([str(10-int(x)) if (int(x) != 5 and int(x) != 0) else '0' if x == '5' else '5' for x in string])   
    #return s.translate(str.maketrans("1234567890", "9876043215"))


print(decode("4103432323"))#, "6957678787")
print(decode("4103438970"))#, "6957672135")
print(decode("4104305768"))#, "6956750342")
print(decode("4102204351"))#, "6958856709")
print(decode("4107056043"))#, "6953504567")

#[unicode(x.strip()) if x is not None else '' for x in row]


##>>> l = [1, 2, 3, 4, 5]
#>>> ['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in l]
#>>> [str(10-int(x)) if (x != 5 and x != 0) else '0' if x == 5 else '5' for x in string]
#['yes', 'no', 'idle', 'idle', 'idle']