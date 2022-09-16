def inorderTraversal(root):
    output = []

    def traversal(node):
        if node.left:
            traversal(node.left)
        output.append(root.val)
        if node.right:
            traversal(node.right)

    traversal(root)
    return output