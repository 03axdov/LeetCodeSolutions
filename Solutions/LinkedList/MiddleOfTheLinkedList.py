import math
def middleNode(head):
    front = current = head
    length = 1
    if not head:
        return

    while current.next:
        current = current.next
        length += 1
    
    middle = length // 2
    count = 0

    while True:
        if count == middle:
            return front
        count += 1
        front = front.next