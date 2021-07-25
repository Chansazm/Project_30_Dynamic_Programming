def gridtravelertab(m,n):
    Table = [[0] * (m+1) for _ in range(n+1)]
    Table[1][1] = 1
    
    for i in range(m):
        for j in range(n):
            current = Table[i][j]
            if j+ 1 <= n:Table[i][j+1] += current
            if i + 1 <= m: Table[i+1][j] += current
    return Table[i][j]







#Driver function
#Time Complexity:: memoised is n * m unmemoised is 2^(n+m)
#Space Complexity:: n + m
print(gridtravelertab(2,3)) # 3
#print(gridtravelertab(1000,1000))# 2333606220