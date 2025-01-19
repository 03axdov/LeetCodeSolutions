from collections import deque

def plusOne(self, digits):
    res = deque([])
    carry = 1
    
    i = len(digits) - 1
    while i >= 0:
        toPrepend = (digits[i] + carry) % 10
        carry = (digits[i] + carry) // 10
        res.appendleft()
        i -= 1
        
    if carry: res.appendleft(carry)
    return list(res)