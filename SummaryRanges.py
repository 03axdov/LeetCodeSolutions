def summaryRanges(nums):
    ranges = []
    currentRangeStart = -1
    currentRangeEnd = -1
    
    for i in range(len(nums)):
        if currentRangeStart == -1 or i == 0: currentRangeStart = i         
        else:
            if nums[i] == nums[i-1] + 1:
                currentRangeEnd = i
            elif currentRangeEnd == -1:
                ranges.append(str(nums[currentRangeStart]))
                currentRangeStart = i
            else:
                ranges.append(str(nums[currentRangeStart]) + "->" + str(nums[currentRangeEnd]))
                currentRangeStart = i
                currentRangeEnd = -1
                
    if currentRangeStart != -1 and currentRangeEnd != -1: ranges.append(str(nums[currentRangeStart]) + "->" + str(nums[currentRangeEnd]))
    elif currentRangeStart != -1: ranges.append(str(nums[currentRangeStart]))
                
    return ranges