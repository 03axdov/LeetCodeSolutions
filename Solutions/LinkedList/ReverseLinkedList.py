class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    reversedValues = []
    current = head
    if not head:
        return
    while current.next:
        reversedValues.append(current.val)
        current = current.next

    reversedValues.append(current.val)
    reversedValues = reversedValues
    output = []
    for t, val in enumerate(reversedValues):
        if t != 0:
            node = ListNode(val=val)
            output.append(node)
            output[t-1].next = node
        else:
            node = ListNode(val=val)
            output.append(node)

    return output[0]