class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def getNumber(node: Optional[ListNode]) -> int:
    current = 0
    exp = 0
    while node:
        current += node.val * (10**exp)
        exp += 1
        node = node.next

    return current

def toLinkedList(i: int) -> Optional[ListNode]:
    numString = str(i)[::-1]
    prev = ListNode(val=int(numString[0]))
    first = prev
    for char in numString[1:]:
        nextNode = ListNode(val=int(char))
        prev.next = nextNode
        prev = nextNode

    return first


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    num1 = getNumber(l1)
    num2 = getNumber(l2)

    return toLinkedList(num1 + num2)
