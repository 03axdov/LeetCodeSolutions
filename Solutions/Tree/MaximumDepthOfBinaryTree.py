def maxDepthHelper(root, depth):
    if not root: return depth
    return max(maxDepthHelper(root.left, depth+1), maxDepthHelper(root.right, depth+1))

def maxDepth(root):
    return max(maxDepth(root.left, 1), maxDepth(root.right, 1))