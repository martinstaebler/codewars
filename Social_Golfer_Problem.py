import string

def social_golfer_problem_1(n, g, d):
    #players = list(string.ascii_uppercase)[0:n]
    
    group = ""
    arr_group = list()

    for i in range(0,d):
        players = string.ascii_uppercase[0:n]
        while len(players) > 0:
            for p in range(len(players)-1,-1, -1):
            #for p in range(0, len(players)):
                if len(group) < g:
                    group = group + players[p]
                    players = players.replace(players[p], "")
                else:
                    arr_group.append(group)
                    group = players[p]
                    players = players.replace(players[p], "")
            
    return arr_group

golfer_dict = dict()

def social_golfer_problem(n, g, d):
    #players = list(string.ascii_uppercase)[0:n]
    
    group = ""
    arr_alldays = list()
    arr_day = list()
    players = string.ascii_uppercase[0:n]

    for golfer in players:
        golfer_dict[golfer] = set()

    for i in range(0,d):
        for p in players:
            
            group = group + p
            if len(group) == g:
                arr_day.append(group)    
                group = ""
            if len(arr_day) == n/g:    
                arr_alldays.append(arr_day.copy())
                arr_day.clear()
    return arr_alldays



print(social_golfer_problem(20, 4, 5))
#print(social_golfer_problem(10, 2, 5))

"""
input [
  ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
  ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
  ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
  ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
  ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']
 ]
 """