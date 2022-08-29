def minSubArrayLen(target, nums):
    l = 0
    output = float("inf")
    current = 0
    idx = 0
    prevIdx = -1

    while idx < len(nums):
        if prevIdx != idx:
            current += nums[idx]
        prevIdx = idx
        if current >= target:
            output = min(output, idx-l+1)
            current -= nums[l]
            l += 1
        else:
            idx += 1

    if output == float("inf"):
        return 0
    return output


print(minSubArrayLen(11, [1,2,3,4,5]))