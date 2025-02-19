def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0: return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    
    left = nums[:mid]
    right = nums[mid+1:]
    
    root.left = self.sortedArrayToBST(left)
    root.right = self.sortedArrayToBST(right)
    
    return root