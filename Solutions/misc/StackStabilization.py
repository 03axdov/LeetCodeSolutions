from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    # Write your code here
    prevDisc = R[0]
    smallestDisc = R[0]
    res = 0
    
    for disc in R[1:]:
        if disc <= prevDisc:
            prevDisc = (prevDisc - disc) + 1
            smallestDisc -= prevDisc
            res += 1
            if prevDisc <= 0: return -1
        else: prevDisc = disc
        
    return res
