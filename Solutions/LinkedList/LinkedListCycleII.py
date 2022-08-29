def detectCycle(head):
    prev = []
    while head.next:
        if head in prev:
            return head
        prev.append(head)
        head = head.next
    return