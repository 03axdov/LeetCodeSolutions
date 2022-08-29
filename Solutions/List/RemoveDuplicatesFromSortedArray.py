def removeDuplicates(nums):
    i = 0
    while i < len(nums):
        if i != 0 and i < len(nums):
            if nums[i-1] == nums[i]:
                nums.remove(nums[i])
                i = -1
        i += 1

    return len(nums)

print(removeDuplicates([1,1,2]))