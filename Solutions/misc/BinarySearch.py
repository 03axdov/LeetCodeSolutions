def search(nums, target):
    l, r = 0, len(nums) - 1
    prev = []
    while l <= r:
        center = (r+l) // 2
        if center in prev:
            return -1
        if nums[center] == target:
            return center
        elif nums[center] > target:
            prev.append(center)
            r = center
        else:
            prev.append(center)
            l = center + 1
    return -1


print(search([2,5], 5))