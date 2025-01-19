def findKthLargest(nums, k):
    arr = [-float("inf") for i in range(k)]
    
    for num in nums:
        i = k - 1
        if arr[i] >= num: continue
    
        while arr[i] < num and i >= 0:
            i -= 1
        
        arr.insert(i+1, num)
        arr.pop()
    
    return arr[-1]    
    
print(findKthLargest([2,1], 2))