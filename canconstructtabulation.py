def canconstructtab(target,wordbank):
    Table = [False for i in range(len(target) + 1)]
    Table[0] = True
    
    for each_value in range(len(Table)):
        if Table[each_value] == True:
            for word in wordbank:
                if target == word[:word]:
                    Table[each_value + len(word)] = True
    return Table[-1]








#Driver function
#Time complexity:: m == len(target),n == len(wordbank) Brute force m*(n^m):: Memoised n*m^2
#Space complexity:: m * m 
print(canconstructtab("abcdef",["ab","abc","ce","def","abcd"]))#True