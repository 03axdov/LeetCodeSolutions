def pivotIndex(nums):
    current = 0
    sums = []

    for num in nums:
        sums.append(num+current)
        current += num

    for t, i in enumerate(sums):
        if t != 0 and t < len(sums):
            if sums[-1] - i == sums[t-1]:
                return t
        elif t == 0:
            if sums[-1] - i == 0:
                return 0
        elif t == len(sums) - 1:
            if i - nums[t] == 0:
                return t

    return -1

print(pivotIndex([1,2,3]))