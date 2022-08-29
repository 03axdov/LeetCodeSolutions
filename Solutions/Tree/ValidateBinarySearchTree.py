def isValidBST(root):
    output = []
    inorder(root, output)

    for i in range(1, len(output)):
        if output[i-1] >= output[i]: return False
    return True

def inorder(self, root, output):
    if not root: return

    self.inorder(root.left, output)
    output.append(root)
    self.inorder(root.right, output)