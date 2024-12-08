views = []

def traverse(self, root, depth):
    if not root: return
    if depth > len(views): 
        views.append(root.val)
    else:
        traverse(root.right)
        traverse(root.left)

def rightSideView(self, root):
    traverse(root, 1)
    return self.views