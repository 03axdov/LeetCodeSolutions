def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    
    res = -float("inf")
    while left < right:
        curr = min(height[left], height[right]) * (right - left)
        res = max(curr, res)
        
        if height[left] < height[right]: left += 1
        else: right -= 1
        
    return res