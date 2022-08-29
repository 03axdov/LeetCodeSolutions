def runningSum(nums):
    current = 0
    output = []
    for num in nums:
        output.append(num + current)
        current += num
    
    return output


print(runningSum([1,2,3,4]))