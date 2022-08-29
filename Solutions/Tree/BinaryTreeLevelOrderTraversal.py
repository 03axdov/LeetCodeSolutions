def levelOrder(root):
    if root == None:
        return 
    queue = []
    results = []
    queue.append(root)
    while queue:
        level = []
        for i in range(len(queue)):
            current_node = queue.pop(0)
            level.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        results.append(level)
    return results