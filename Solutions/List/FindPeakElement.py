def findPeakElement(nums):
    for i in range(0, len(nums), 2):  
        if i == len(nums) - 1:
            if nums[i-1] < nums[i]:
                return i
        if i == 0:
            if len(nums) == 1:
                return 0
            if nums[i+1] < nums[i]:
                return i
        elif nums[i] < nums[i-1] > nums[i-2]:
            print("A")
            return i - 1
        else:
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i
    return len(nums) - 1


print(findPeakElement([1,2,1]))