def fibtabulation(n):
    Table = [0] * (n + 1)
    Table[1] = 1
    print(Table)
    
    for i in range(n+1):
        if i+2 < n+1:
            Table[i+1] += Table[i]
            Table[i+2] += Table[i]
    return Table[n]


#Driver function
#Time complexity:: Linear with memoized solution and 2^n not memoised
#Time complexity is the branching factor to the height power
#Space complexity is linear
print(fibtabulation(6))

