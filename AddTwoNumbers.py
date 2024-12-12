# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        res = ListNode(-1)
        head = res
        
        while l1 or l2 or carry:
            if not l1 and not l2:
                res.next = ListNode(carry)
                res = res.next
                carry = 0
            elif not l1:
                s = carry + l2.val
                res.next = ListNode(s % 10)
                res = res.next
                l2 = l2.next
                carry = s // 10
            elif not l2:
                s = carry + l1.val
                res.next = ListNode(s % 10)
                res = res.next
                l1 = l1.next
                carry = s // 10
            else:
                s = carry + l1.val + l2.val
                res.next = ListNode(s % 10)
                res = res.next
                l1 = l1.next
                l2 = l2.next
                carry = s // 10
            
        return head.next