def cansum(targetsum, numbers, memo = {}):
    if targetsum in memo: return memo[targetsum]
    if targetsum == 0: return True
    if targetsum < 0: return False
    
    for num in numbers:
        remainder = targetsum - num
        if cansum(remainder,numbers, memo) == True:
            memo[targetsum] = True
            return memo[targetsum]
    return False
               
#Driver function
#Time:: Brute force n^m and memoised m * n
#Space:: m height of the tree basically both memoised and brute force
print(cansum(7,[5,3,4,7])) #True
print(cansum(3000,[5,3,4,7])) #True



