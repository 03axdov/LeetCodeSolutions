def rob(nums):
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums[0], nums[1])

    cash = [0] * len(nums)
    cash[0], cash[1] = nums[0], nums[1]
    for i in range(2, len(nums)):
        cash[i] = max(cash[:i-1]) + nums[i]
    
    return max(cash)


print(rob([1, 1, 2]))