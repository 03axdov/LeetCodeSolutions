def wordPattern(self, pattern: str, s: str) -> bool:
    dic = {}
    seen = set()
    s = s.split(" ")
    if len(s) != len(pattern): return False
    
    for i in range(len(pattern)):
        if pattern[i] not in dic.keys():
            if s[i] in seen: return False
            dic[pattern[i]] = s[i]
            seen.add(s[i])
        elif s[i] != dic[pattern[i]]: return False
        
    return True