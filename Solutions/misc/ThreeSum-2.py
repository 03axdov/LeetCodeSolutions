def threeSum(nums):
    current = {}
    target = 0
    output = []
    for t1, num1 in enumerate(nums):
        target = 0 - num1
        if t1 < len(nums) - 2:
            for num2 in nums[t1+1:]:
                if num2 not in current.keys():
                    current[target-num2] = num2
                else:
                    if sorted([num1, num2, current[num2]]) not in output:
                        output.append(sorted([num1, num2, current[num2]]))
            current = {}
    
    return output


print(threeSum([0,1,1]))