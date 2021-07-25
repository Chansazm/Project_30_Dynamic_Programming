def countconstruct(target, wordbank, memo = {}):
    if target in memo: return memo[target]
    if target == '': return 1
    
    totalways = 0
    for word in wordbank:
        if target[0] == word[0]:
            suffix = target[len(word):]
            numofways = countconstruct(suffix,wordbank, memo)
            totalways += numofways
    memo[target] = totalways
    return memo[target]









#Driver function
#Time complexity:: m == len(target),n == len(wordbank) Brute force m*(n^m):: Memoised n*m^2
#Space complexity:: m * m 
print(countconstruct("abcdef",["ab","abc","ce","def","abcd"])) #1