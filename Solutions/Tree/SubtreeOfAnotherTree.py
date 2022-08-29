def isSubtree(root, subRoot):
    if not root or not subRoot:
        return False
    if isSameTree(root, subRoot):
        return True

    def isSameTree(r, sr):
        if not r or not sr:
            return False
        if r.val == sr.val and isSameTree(r.left, sr.left) and isSameTree(r.right, sr.right):
            return True
        return False
    
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)