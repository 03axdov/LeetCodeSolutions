pointer = None

def flatten(self, root: Optional[TreeNode]) -> None:
    if not root: return
    leftNode = root.left
    rightNode = root.right
    
    root.left = None
    self.pointer = root
    
    self.preorderTraversal(leftNode)
    self.preorderTraversal(rightNode)
    
    
def preorderTraversal(self, root):
    if root == None: return

    tempLeft = root.left
    tempRight = root.right

    temp = root
    temp.left = None
    self.pointer.right = temp
    self.pointer = temp
    
    self.preorderTraversal(tempLeft)
    self.preorderTraversal(tempRight)