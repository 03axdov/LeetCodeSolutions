def invertTree(self, root):
    if not root: return None
    l = root.left
    root.left = self.invertTree(root.right)
    root.right = self.invertTree(root.left)
    
    return root