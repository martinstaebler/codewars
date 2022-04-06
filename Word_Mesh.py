# https://www.codewars.com/kata/5c1ae703ba76f438530000a2/train/python

def word_mesh_2(words):
    solution_string = ""

    for i in range(0, len(words)-1):
        if words[i][-1] in words[i+1]:
            len_slice = -1 * len(words[i+1][:words[i+1].index(words[i][-1])+2])

            char_slice = words[i+1][:words[i+1].index(words[i][-1])+2]
            print(char_slice)
            if char_slice == words[i][len_slice:]:
                solution_string += char_slice
                
            else: 
                len_slice = -1 * len(words[i+1][:words[i+1].index(words[i][-1])+1])
                char_slice = words[i+1][:words[i+1].index(words[i][-1])+1]
                if char_slice == words[i][len_slice:]:
                    solution_string += char_slice
                else:
                    print(solution_string)
                    return "failed to mesh"
    return solution_string

def word_mesh(words):
    solution_string = ""
    for i in range(0, len(words)-1):
        counter = 0
        word_slice = ""
        while counter <= len(words[i]) and counter <= len(words[i+1]):
            if words[i][-1 * counter:] == words[i+1][:counter]:
                word_slice = words[i][-1 * counter:]
            counter += 1
        
        if len(word_slice) > 0:
            solution_string += word_slice
        else:
            return "failed to mesh"

    return solution_string
   
#print(word_mesh(["beacon", "condominium", "umbilical", "california"]))#, "conumcal")
#print(word_mesh(["allow", "lowering", "ringmaster", "terror"]))#, "lowringter")
#print(word_mesh(["abandon", "donation", "onion", "ongoing"]))#, "dononon")
#print(word_mesh(["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]))#, "ownhippuscartpher")
#print(word_mesh(['marker', 'kerchief']))#'kereflesssonnetworkokma'
print(word_mesh(['marker', 'kerchief', 'effortless', 'lesson', 'sonnet', 'network', 'workbook', 'oklahoma', 'marker']))#'kereflesssonnetworkokma'
#print(word_mesh(['parisinfrance', 'franceineurope', 'europeonearth', 'earthinthesolarsystem', 'systematicallygettingbigger']))#'franceeearthsystem' should equal 'franceeuropeearthsystem'