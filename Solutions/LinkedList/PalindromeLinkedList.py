def isPalindrome(head):
    nodes = []
    while head.next:
        nodes.append(head.val)
        head = head.next

    nodes.append(head.val)

    l,r = 0, len(nodes) - 1
    while l <= r:
        if nodes[l] == nodes[r]:
            r -= 1
            l += 1
            continue
        else:
            return False
    return True