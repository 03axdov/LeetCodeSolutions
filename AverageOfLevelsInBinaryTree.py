def averageOfLevels(self, root):
    levelSum = []
    levelCount = []
    
    self.traverse(root, levelSum, levelCount, 0)
    
    res = []
    for i in range(len(levelSum)):
        res.append(levelSum[i] / levelCount[i])
        
    return res
    
    
def traverse(self, root, levelSum, levelCount, level):
    if not root: return
    if len(levelSum) < level + 1: 
        levelSum.append(0)
        levelCount.append(0)
        
    levelCount[level] += 1
    levelSum[level] += root.val
    
    self.traverse(root.left, levelSum, levelCount, level+1)
    self.traverse(root.right, levelSum, levelCount, level+1)