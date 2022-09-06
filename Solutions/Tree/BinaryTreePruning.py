def pruneTree(root):
    def traversal(node):
        if not node.left and not node.right and node.val == 0: return False
        if not node.left and not node.right and node.val == 1: return True

        if node.left:
            if not traversal(node.left):
                node.left = None

        if node.right:
            if not traversal(node.right):
                node.right = None

        if node.val == 1:
            return True
        else:
            return node.right or node.left

    traversal(root)
    if not root.left and not root.right and not root.val: return

    return root