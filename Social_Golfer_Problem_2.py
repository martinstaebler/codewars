# https://www.codewars.com/kata/556c04c72ee1147ff20000c9

def valid(a):
    dict_players = {}

    for i in a:
        if "".join(sorted("".join(i))) != "".join(sorted("".join(a[0]))):
            return False

        if show_doubles(i):
            return False

        for j in range(0, len(i)):
            if len(i[0]) != len(i[j]):
                print("false: group size not equal") 

            for k in i[j]:
                if k in dict_players:
                    dict_players[k] += list(i[j].replace(k,""))
                else:
                    dict_players[k] = list(i[j].replace(k,""))

            # Dictionary auf Doubles prüfen
    for key in dict_players:
        if show_doubles(["".join(dict_players[key])]):
            return False
    #print(dict_players)
    return True

def show_doubles(group):
    
    return True if len("".join(group)) != len(set("".join(group))) else False

golfer_1 = [
    ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
    ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
    ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
    ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
    ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']]

golfer_2 = [
    ["AB", "CD"],
    ["AD", "BC"],
    ["BD", "AC"]] 

golfer_3 = [
    ["AB", "CD", "EF", "GH"],
    ["AC", "BD", "EG", "FH"],
    ["AD", "CE"],
    ["AE", "BG", "CH", "FD"]]

golfer_4 = [
    ["ABC", "DEF"],
    ["ADE", "CBF"]]    

print(valid(golfer_1))
print(valid(golfer_2))
print(valid(golfer_3))
print(valid(golfer_4))