def canconstruct(target,wordbank,memo={}):
    if target in memo: return memo[target]
    if target == '': return True

    for word in wordbank:
        if target[0] == word[0]:
            suffix = target[len(word):]
            if canconstruct(suffix,wordbank) == True:
                memo[target] = True
                return memo[target]
    return False









#Driver function
#Time complexity:: m == len(target),n == len(wordbank) Brute force m*(n^m):: Memoised n*m^2
#Space complexity:: m * m 
print(canconstruct("abcdef",["ab","abc","ce","def","abcd"])) #True