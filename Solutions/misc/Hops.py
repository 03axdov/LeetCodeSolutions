from typing import List
# Write any import statements here

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    res = 0
    P = list(sorted(P))
    prevPad = P[0]
    
    for pad in P[1:]:
        res += pad - prevPad - 1
        prevPad = pad
    
    res += N - P[-1] - 1
    res += F
    return res