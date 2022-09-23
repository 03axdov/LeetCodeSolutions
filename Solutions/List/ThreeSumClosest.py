def threeSumClosest(nums, target: int) -> int:
    closest = float("inf")

    nums = sorted(nums)

    print(nums)
    for i in range(len(nums) - 1):
        l = i+1
        r = len(nums) - 1
        currentClosest = float("inf")
        while l < r:
            if abs(target - (nums[i] + nums[l] + nums[r])) < abs(target - currentClosest):
                currentClosest = (nums[i] + nums[l] + nums[r])
            else:
                break

            if nums[i] + nums[l] + nums[r] < target:
                l += 1
            elif nums[i] + nums[l] + nums[r] > target:
                r -= 1
            else:
                return target

        if abs(target-currentClosest) < abs(target-closest):
            closest=currentClosest

    return closest


print(threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))