from collections import deque

def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    self.traverse(root, res, 0)
    
    return list(res)
    
    
def traverse(self, root, res, level):
    if not root: return
    leftToRight = level % 2 == 0
    if len(res) < level + 1:
        res.append([])
    
    if leftToRight:
        res[level].append(root.val)
    else:
        res[level] = [root.val] + res[level]
                
    self.traverse(root.left, res, level+1)
    self.traverse(root.right, res, level+1)