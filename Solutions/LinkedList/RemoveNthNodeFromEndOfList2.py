def removeNthFromEnd(head, n: int):
    nodes = []
    node = head

    while node.next:
        nodes.append(node)
        node = node.next

    nodes.append(node)

    if len(nodes) == 1:
        return

    if n == 1:
        nodes[-2].next = None
    elif n == len(nodes):
        return nodes[1]
    else:
        nodes[-n-1].next = nodes[-n+1]
    
    return nodes[0]