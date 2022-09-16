from collections import deque
def maximumScore(nums, multipliers) -> int:
    score = 0
    nums = deque(nums)

    for i in multipliers:
        if nums[-1] * i < nums[0] * i:
            score += nums.popleft() * i
        else:
            score += nums.pop() * i

    return score


print(maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))