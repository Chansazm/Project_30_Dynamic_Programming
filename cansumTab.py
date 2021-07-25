def cansumtab(targetsum,numbers):
    Table = [False] * (targetsum + 1)
    Table[0] = True
    
    for i in range(targetsum):
        if Table[i] == True:
            for num in numbers:
                if i+ num <= targetsum:
                    Table[i+num] = True
    return Table[targetsum]

#Driver function
#Time:: Brute force n^m and memoised m * n
#Space:: m height of the tree basically both memoised and brute force
print(cansumtab(3,[0,1,2,3])) #True
print(cansumtab(3000,[5,3,4,7])) #True