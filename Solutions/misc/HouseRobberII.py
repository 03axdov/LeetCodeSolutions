def rob(nums):
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums[0], nums[1])
    output = []

    for i in range(2):
        currentNums = nums[i:i+len(nums)-1]
        
        cost = [0] * (len(currentNums))
        cost[0] = currentNums[0]
        cost[1] = currentNums[1]

        for i in range(2, len(currentNums)):
            cost[i] = max(cost[:i-1]) + currentNums[i]
        output.append(max(cost))
    
    return max(output)


print(rob([1,2,3]))