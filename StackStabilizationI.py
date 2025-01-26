from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    # Write your code here
    res = 0
    prevDisc = R[-1]
    for disc in reversed(R[:-1]):
        if disc >= prevDisc:
            prevDisc -= 1
            res += 1
            if prevDisc <= 0: return -1
        else: prevDisc = disc

    return res