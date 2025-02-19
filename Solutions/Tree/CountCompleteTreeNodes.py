# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # find the deepest level
        node = root
        max_depth = 0
        while node.left:
            node = node.left
            max_depth += 1

        # initialise binary path for directions to check if a node exists
        path = [0] * max_depth
        if path: 
            path[0] = 1

        i = 0
        while i < max_depth:
            node = root
            depth = 0
            while depth < max_depth:
                node = node.right if path[depth] else node.left  # turn left if 0, turn right if 1
                depth += 1
            if not node:
                path[i] = 0  # if node not found, take left turn next iteration
            if i + 1 < len(path):
                path[i+1] = 1  # default to taking right turn at next level down
            i += 1
        bin_res_str = ''.join(map(str, path))
        res = int('1' + bin_res_str, 2)  # '1' + binary path computes the total no. of nodes 
        return res