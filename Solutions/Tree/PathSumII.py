class Solution:
    paths = []

    def traversal(self, node, currentPath):
        c = currentPath.copy()
        c.append(node.val)
        if not node.left and not node.right:
            self.paths.append(c)
        else:
            self.traversal(node.left, c)
            self.traversal(node.right, c)
        

    def pathSum(self, root, targetSum: int):
        self.paths = []
        output = []
        self.traversal(root)

        for path in self.paths:
            if sum(path) == targetSum:
                output.append(path)

        return output