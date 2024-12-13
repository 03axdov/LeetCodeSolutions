def searchInsert(self, nums, target):
    h = len(nums) - 1
    l = 0
    
    while l <= h:
        idx = (h + l) // 2
        if nums[idx] > target:
            h = idx - 1
        elif nums[idx] < target:
            l = idx + 1
        else: return idx
            
        
    return l