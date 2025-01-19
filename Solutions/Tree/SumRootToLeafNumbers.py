class Solution(object):
    allNumbers = []
    def sumNumbers(self, root):
        self.traverse(root, "")
        
        return sum(map(int, self.allNumbers))


    def traverse(self, root, currentPath):
        if not root: return
        if not root.left and not root.right:
            self.allNumbers.append(currentPath + str(root.val))
            return
        
        newPath = currentPath + str(root.val)
        self.traverse(root.left, newPath)
        self.traverse(root.right, newPath)