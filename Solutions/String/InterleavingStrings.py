dic = {}

def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3): return False
    if len(s1) <= len(s2): return self.isInterleave(s2, s1, s3)
    
    if (s1, s2) in self.dic.keys(): return dic[(s1, s2)]
    
    p1 = 0
    p2 = 0
    
    idx = 0
    branches = []
    while idx < len(s3) or p1 < len(s1) or p2 < len(s2):
        if p1 >= len(s1): return s2[p2:] == s3[idx:]
        elif p2 >= len(s2): return s1[p1:] == s3[idx:]
    
        if s1[p1] == s3[idx] and s2[p2] == s3[idx]:
            self.dic[(s1[p1+1:], s2[p2:])] = self.isInterleave(s1[p1+1:], s2[p2:], s3[idx+1:])
            branches.append(self.dic[(s1[p1+1:], s2[p2:])])
            p2 += 1
        elif s1[p1] == s3[idx]:
            p1 += 1
        elif s2[p2] == s3[idx]:
            p2 += 1
        else:
            return True in branches
        
        idx += 1
        
    return (p1 == len(s1) and p2 == len(s2)) or (True in branches)