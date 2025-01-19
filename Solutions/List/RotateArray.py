def rotate(self, nums, k):
    k = k % len(nums)
    for _ in range(k):
        r = nums.pop()
        nums.insert(0, r)