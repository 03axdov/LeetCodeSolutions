def levelOrder(root):
    currentLevel = 0
    output = []

    def traversal(node, currentLevel):
        if len(output) < currentLevel + 1:
            output.append([node.val])

        else:
            output[currentLevel].append(node.val)

        for child in node.children:
            traversal(child, currentLevel + 1)


    traversal(root, currentLevel)
