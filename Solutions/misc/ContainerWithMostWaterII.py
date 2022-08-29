def maxArea(height):
    l, r = 0, len(height) - 1
    currentMax = 0

    while l < r:
        currentMax = max(currentMax, min(height[l], height[r]) * (r-l))
        if height[r] >= height[l]:
            l += 1
        else:
            r -= 1
        
    return currentMax


print(maxArea([1,8,6,2,5,4,8,3,7]))