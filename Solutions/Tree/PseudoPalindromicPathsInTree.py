from collections import deque, Counter
class Solution:
    output = 0
    def traversal(self, node, pairs):
        p = pairs.copy()
        if node.val in p:
            p.remove(node.val)
        else:
            p.add(node.val)

        if node.left:
            self.traversal(node.left, p)
        if node.right:
            self.traversal(node.right, p)

        if not node.left and not node.right:
            if len(p) == 1 or len(p) == 0:
                self.output += 1

    def pseudoPalindromicPaths(self,root):
        self.traversal(root, set())
        return self.output