def cansum(targetsum, numbers):
    if targetsum == 0: return True
    if targetsum < 0: return False
    
    for num in numbers:
        remainder = targetsum - num
        if cansum(remainder,numbers) == True:
            return True
    return False
               
#Driver function
#Time::
#Space::
print(cansum(7,[5,3,4,7])) #True



