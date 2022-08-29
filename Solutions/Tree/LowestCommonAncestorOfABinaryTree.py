def lowestCommonAncestor(self, root, p, q):
    if max(p.val, q.val) < root.val:
        return self.lowestCommonAncestor(root.left, p, q)
    elif min(p.val, q.val) > root.val:
        return self.lowestCommonAncestor(root.right, p, q)
    else:
        return root