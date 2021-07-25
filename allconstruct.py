def allconstruct(target,wordbank):
    if target == '': return []
    
    result = []
    for word in wordbank:
        if target[0] == word[0]:
            suffix = target[len(word):]
            suffixwaysways = allconstruct(suffix,wordbank)
            #targetways = suffixwaysways.map(way => [word,...way])
            targetways = map(lambda x: x + x, word,suffixwaysways)
    result.append(targetways)


#Driver function
#m = targetsum
#Time complexity:: Brute force n^m * m^2, memoised n * m
#Space complexity:: height of the tree m, memoised m*m
print(allconstruct("abcdef",["ab","abc","ce","def","abcd"]))