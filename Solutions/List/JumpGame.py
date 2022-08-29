def canJump(nums):
    maxIdx = 0
    for t, num in enumerate(nums):
        if t > maxIdx:
            return False
        maxIdx = max(maxIdx, num+t)
    return True


print(canJump([3,2,1,0,4]))