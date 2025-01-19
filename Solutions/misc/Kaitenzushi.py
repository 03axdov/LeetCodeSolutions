from collections import deque

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    # Write your code here
    prevK = set()
    toRemove = deque()
  
    res = 0
    for d in D:
        if d not in prevK:
            res += 1
            prevK.add(d)
            toRemove.appendleft(d)
            if (len(toRemove) > K):
                prevK.remove(toRemove.pop())
              
    return res