from typing import List
def largestPerimeter(nums: List[int]) -> int:
    nums = sorted(nums)
    for i in range(len(nums) - 3, 0 , -1):
        if nums[i] + nums[i+1] > nums[i+2]:
            return nums[i] + nums[i+1] + nums[i+2]

    if nums[0] + nums[1] > nums[2]: return nums[0] + nums[1] + nums[2]
    return 0

print(largestPerimeter([2,3,3,4]))