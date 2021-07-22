import sys

sys.setrecursionlimit(100000)

def fib(n,memo = {}):
    if n in memo: return memo[n]
    if n <= 2: return 1
    else:
        memo[n] = fib(n-1,memo) + fib(n-2,memo)
        return memo[n]

#Driver function
#Time complexity:: Linear with memoized solution and 2^n not memoised
#Space complexity is linear
print(fib(5000))