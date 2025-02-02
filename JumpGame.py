def canJump(self, nums: List[int]) -> bool:
    currentMax = nums[0]
    
    for i in range(len(nums)):
        if currentMax >= len(nums)-1: return True
        if nums[i] == 0 and currentMax <= i: return False
        
        currentMax = max(currentMax, i + nums[i])
        
    return True