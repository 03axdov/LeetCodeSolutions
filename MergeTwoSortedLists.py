def mergeTwoLists(self, list1, list2):
    curr = None
    if not list1:
        return list2
    if not list2:
        return list1
        
    if list1.val < list2.val: 
        curr = list1
        list1 = list1.next
    else:
        curr = list2
        list2 = list2.next
    
    h = curr
    while list1 or list2:
        if not list1: 
            curr.next = list2
            list2 = list2.next
            curr = curr.next
        elif not list2:
            curr.next = list1
            list1 = list1.next
            curr = curr.next    
        elif list1.val < list2.val:
            curr.next = list2
            list2 = list2.next
            curr = curr.next
        else:
            curr.next = list1
            list1 = list1.next
            curr = curr.next  
            
    return h