def maxSubArray(self, nums: List[int]) -> int:
    res = -float("inf")
    tot = 0
    
    for i in nums:
        tot = max(0, tot)
        tot += i
        
        res = max(res,tot)
    
    return res