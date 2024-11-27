def removeDuplicates(nums):
    currentIdx = 2
    if len(nums) < 2: return len(nums)
    
    for i in range(2, len(nums)):
        if nums[currentIdx-1] != nums[i] or nums[currentIdx-2] != nums[i]:
            nums[currentIdx] = nums[i]
            currentIdx += 1

    return currentIdx