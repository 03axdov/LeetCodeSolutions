def searchRange(nums, target):
    l,r = 0, len(nums) - 1
    output = [-1, -1]

    while l <= len(nums) - 1 and r >= 0 and l <= r:
        middle = (l+r) // 2
        if nums[middle] > target:
            r = middle - 1
        elif nums[middle] < target:
            l = middle + 1
        else:
            l, r = middle, middle
            while True:
                if l > 0 and output[0] == -1:
                    if nums[l-1] != target:
                        output[0] = l
                        if output[1] != -1:
                            return output
                elif output[0] == -1:
                    output[0] = l
                    if output[1] != -1:
                        return output
                if r < len(nums) - 1 and output[1] == -1:
                    if nums[r+1] != target:
                        output[1] = r
                        if output[0] != -1:
                            return output
                elif output[1] == -1:
                    output[1] = r
                    if output[0] != -1:
                        return output
                r += 1
                l -= 1
    return output
                    

print(searchRange([0,0,1,2,2], 2))