def removeElement(nums, val):
    res = len(nums)
    toReplace = []
    
    for i in range(len(nums)):
        if nums[i] == val:
            res -= 1
            toReplace.append(i)
        elif len(toReplace) > 0:
            nums[toReplace.pop(0)] = nums[i]
            toReplace.append(i)
            
    return res