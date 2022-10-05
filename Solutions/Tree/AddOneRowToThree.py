class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def addOneRow(root, val: int, depth: int):
    def traversal(node, currentDepth):
        if currentDepth == depth - 1:
            newNodeLeft = TreeNode(val=val, left=node.left)
            newNodeRight = TreeNode(val=val, right=node.right)
            node.left = newNodeLeft
            node.right = newNodeRight
        else:
            if node.left:
                traversal(node.left, currentDepth+1)
            if node.right:
                traversal(node.right, currentDepth+1)

    if depth == 1:
        output = TreeNode(val=val, left=root)
        return output

    traversal(root, 1, 0)
    return root