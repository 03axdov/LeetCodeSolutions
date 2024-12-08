def hasCycle(head):
    fast = head
    slow = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        
        if fast == slow: return True
    
    return False