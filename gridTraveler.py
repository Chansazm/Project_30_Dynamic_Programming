import sys
sys.setrecursionlimit(100000)

def gridtraveler(m,n,memo = {}):
    key = m,n
    if key in memo: return memo[key]
    if m == 0 or n == 0: return 0
    if m == 1 and n == 1: return 1
    
    memo[key] = gridtraveler(m-1,n,memo) + gridtraveler(m,n-1,memo)
    return memo[key]
    




#Driver function
#Time Complexity:: memoised is n * m unmemoised is 2^(n+m)
#Space Complexity:: n + m
print(gridtraveler(2,3)) # 3
print(gridtraveler(1000,1000))# 2333606220