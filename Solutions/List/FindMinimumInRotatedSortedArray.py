def findMin(nums):
    l, r = 0, len(nums) - 1
    middle = (l+r)//2
    initial = middle
    while l <= r:
        middle = (l+r)//2
        if middle >= 1:
            if nums[middle - 1] > nums[middle]:
                return nums[middle]
        if nums[middle] < nums[initial]:
            r = middle - 1
        elif middle == len(nums) - 1:
            if nums[0] <= nums[middle]: # Only < would return None for lists of length 1
                return nums[0]
            else:
                r = initial - 1
                l = 0
        else:
            l = middle + 1


print(findMin([1]))