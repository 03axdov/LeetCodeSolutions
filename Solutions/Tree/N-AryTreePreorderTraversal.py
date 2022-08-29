def preorder(root):
    output = []
    if not root:
        return

    def traversal(node):
        output.append(node.val)
        for child in node.children:
            traversal(child)

    traversal(root)
    return output