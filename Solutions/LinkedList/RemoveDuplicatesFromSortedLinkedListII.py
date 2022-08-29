from collections import defaultdict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    count = defaultdict(int)
    values = []
    if not head:
        return
    while head.next:
        if count[head.val] == 0:
            count[head.val] += 1
            values.append(head.val)
        elif count[head.val] != -1:
            values.remove(head.val)
            count[head.val] = -1
        head = head.next

    if count[head.val] == 0:    # The last node
        values.append(head.val)
    elif count[head.val] != -1:
        values.remove(head.val)

    output = []

    for t, value in enumerate(values):
        node = ListNode(val=value)
        if t != 0:
            output[-1].next = node
        output.append(node)

    if output:
        return output[0]
    return