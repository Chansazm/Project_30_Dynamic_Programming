def howsumtab(targetsum, numbers):
    Table = [None] * (targetsum + 1)
    Table[0] = []
    
    for i in range(targetsum):
        if Table[i] != None:
            for num in numbers:
                    Table[i+num] = [Table[i],num]
    return Table[targetsum]







#Driver function
#m = targetsum
#Time complexity:: Brute force n^m * m^2, memoised n * m
#Space complexity:: height of the tree m, memoised m*m
print(howsumtab(7,[5,3,4]))
#print(howsumtab(30,[5,3,4,7]))