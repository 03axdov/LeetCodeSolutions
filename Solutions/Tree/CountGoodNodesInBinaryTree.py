class Solution:
    output = 0
    def goodNodes(self, root) -> int:
        currentPath = []
        self.traverse(root, currentPath)
        return self.output

    def traverse(self, root, currentPath):
        if root.left or root.right:
            currentPath.append(root.val)
            if not currentPath:
                self.output += 1
            elif root.val >= max(currentPath):
                self.output += 1
            if root.left:
                self.traverse(root.left, currentPath)
            if root.right:
                self.traverse(root.right, currentPath)
            currentPath.pop()
        else:
            if not currentPath:
                self.output += 1
            elif root.val >= max(currentPath):
                self.output += 1
