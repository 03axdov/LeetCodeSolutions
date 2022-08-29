class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    outputNode = current = ListNode(0)
    while list1 and list2:
        if list1.val > list2.val:
            current.next = list2.val
            list2 = list2.next
        else:
            current.next = list1.val
            list1 = list1.next
        current = current.next

    if list1:
        current.next = list1
    if list2:
        current.next = list2
    return outputNode.next
