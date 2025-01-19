class Solution(object):
    dic = {}

    def rob(self, nums):
        self.dic = {}
        return self.robInner(nums, 0)

    def robInner(self, nums, currentIdx):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        if currentIdx not in self.dic.keys():
            self.dic[currentIdx] = max(nums[0] + self.rob(nums[2:], currentIdx + 2), self.rob(nums[1:], currentIdx + 1))
        return self.dic[currentIdx]