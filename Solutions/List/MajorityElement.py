def majorityElement(nums):
    res = 0
    majority = 0
    
    for num in nums:
        if majority == 0:
            res = num
            
        if num == res:
            majority += 1
        else: 
            majority -= 1
            
    return res