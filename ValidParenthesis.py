from collections import deque

def isValid(s):
    q = deque()
    openingBrackets = set(['(', '{', '['])
    mapped = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        if char in openingBrackets:
            q.appendleft(char)
        else:
            if len(q) == 0: return False
            toClose = q.popleft()
            if mapped[toClose] != char: return False
            
    return len(q) == 0


print(isValid("()[]{}"))