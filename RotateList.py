def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    nodes = [head]
    if not head: return None
    if not head.next: return head
    if k == 0: return head
    
    current = head
    while current.next:
        nodes.append(current.next)
        current = current.next
        
    rotate = k % len(nodes)
    if rotate == 0: return head
    newHead = nodes[-1 * rotate]
    newTail = nodes[-1 * rotate - 1]
    newTail.next = None
    current.next = head

    return newHead