from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S = sorted(S)
    l = 0
    r = 1
    
    res = (S[0] - 1) // (K + 1)
    while r < len(S):
        res += max(0, (S[r] - S[l] - 1 - K) // (K + 1))
        l += 1
        r += 1
    
    res += (N - S[-1]) // (K + 1)
    
    return res
    


N = 15
K = 2
M = 3
S = [11, 6, 14]

print(getMaxAdditionalDinersCount(N, K, M, S))