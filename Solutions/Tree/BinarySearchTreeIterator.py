from collections import deque

def traverse(root, d):
    if not root: return
    traverse(root.right, d)
    d.appendleft(root.val)
    traverse(root.left, d)


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.d = deque([])
        traverse(root, self.d)
        

    def next(self):
        """
        :rtype: int
        """
        return self.d.popleft()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.d) > 0