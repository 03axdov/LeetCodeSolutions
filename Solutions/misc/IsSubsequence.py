def isSubsequence(s, t):
    for c in s:
        if c not in t:
            return False
        else:
            t = t[(t.index(c)+1):]
    return True



print(isSubsequence("abc", "ahbgdc"))