import sys

sys.setrecursionlimit(10000000)

def howsum(target,numbers,memo = {}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None
    
    for num in numbers:
        remainder = target - num
        remainder_sum = howsum(remainder,numbers,memo)
        if remainder_sum != None:
            memo[target] = [*remainder_sum,num]
            return memo[target]
    return None

#Driver function
#m = targetsum
#Time complexity:: Brute force n^m * m^2, memoised n * m
#Space complexity:: height of the tree m, memoised m*m
print(howsum(7,[5,3,4,7]))
print(howsum(30000,[5,3,4,7]))