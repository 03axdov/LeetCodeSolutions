def maxArea(height):
    current_max = 0
    l, r = 0, len(height) - 1

    while l < r:
        current_max = max(current_max, min(height[l], height[r]) * (r-l))
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return current_max

print(maxArea([1,8,100,2,100,4,8,3,7]))