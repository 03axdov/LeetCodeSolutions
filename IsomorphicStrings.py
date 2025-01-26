def isIsomorphic(self, s: str, t: str) -> bool:
    dicS = {}
    seen = set()
    
    if len(s) != len(t): return False
    for i in range(len(s)):
        if s[i] not in dicS.keys():
            if t[i] in seen: return False
            dicS[s[i]] = t[i] 
        
        seen.add(t[i])
        if dicS[s[i]] != t[i]: return False
        
    return True