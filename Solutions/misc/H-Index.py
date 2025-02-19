from typing import List

def hIndex(citations: List[int]) -> int:
    citations = sorted(citations)

    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i
    
    return 0


print(hIndex([1,3,1]))