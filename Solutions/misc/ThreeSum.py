def threeSum(nums):
    result = []
    nums = sorted(nums)

    for t in range(len(nums)):
        l, r = t+1, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] + nums[t] < 0:
                l += 1
            elif nums[l] + nums[r] + nums[t] > 0:
                r -= 1
            else:
                if sorted([nums[t], nums[l], nums[r]]) not in result:
                    result.append(sorted([nums[t], nums[l], nums[r]]))
                l += 1
                if nums[l-1] == nums[l] and l < r:
                    l += 1

    return result


print(threeSum([-1,0,1,2,-1,-4]))