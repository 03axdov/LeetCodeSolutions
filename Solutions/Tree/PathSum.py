def hasPathSum(root, targetSum: int) -> bool:
    def traversal(node, currentSum):
        c = currentSum + node.val

        if node.left and node.right:
            return traversal(node.left, c) or traversal(node.right, c)
        elif node.left:
            return traversal(node.left, c)
        elif node.right:
            return traversal(node.right, c)
        else:
            return currentSum == targetSum

    return traversal(root, 0)