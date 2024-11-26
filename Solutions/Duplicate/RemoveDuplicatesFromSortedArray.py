def removeDuplicates( nums):
    seenNums = set()
    res = 0

    for i in range(len(nums)):
        nextNewElement = i + 1
        while nums[i] in seenNums:
            if nextNewElement == len(nums): return res
            
            if nums[nextNewElement] not in seenNums:
                nums[i] = nums[nextNewElement]
                
            nextNewElement += 1

        seenNums.add(nums[i])
        res += 1
        
    return res