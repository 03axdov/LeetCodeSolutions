
class Solution:
    levels = []
    def averageOfLevels(self, root):
        currentLevel = 0
        output = []

        self.traverse(root, currentLevel)

        for level in self.levels:
            output.append(sum(level) / len(level))

        return output

    def traverse(self, root, currentLevel):
        if currentLevel < len(self.levels):
            self.levels[currentLevel].append(root.val)
        else:
            self.levels.append([root.val])

        if root.left:
            self.traverse(root.left, currentLevel + 1)
        if root.right:
            self.traverse(root.right, currentLevel + 1)