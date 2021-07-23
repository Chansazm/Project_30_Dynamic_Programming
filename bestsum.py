def bestsum(targetsum,numbers,memo = {}):
    if targetsum in memo: return memo[targetsum]
    if targetsum < 0: return None
    if targetsum == 0: return []
    shortest_combination = None
    
    for num in numbers:
        remainder = targetsum - num
        results = bestsum(remainder,numbers,memo)
        if results != None:
            combination = [*results,num]
            if shortest_combination == None or len(combination) < len(shortest_combination):
                shortest_combination = combination          
    
    memo[targetsum] = shortest_combination
    return memo[targetsum]

#Driver function
# m is target and n is len(numbers)
#Time complexity:: 
#Space complexity::
print(bestsum(7,[5,3,4,7])) #7
print(bestsum(8,[2,3,5])) # [5,3]
print(bestsum(100,[1,2,5,25]))