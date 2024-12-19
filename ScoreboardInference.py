from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  isOdd = 0
  maxNum = -float("inf")
  
  for s in S:
    if s % 2 != 0: isOdd = 1
    maxNum = max(maxNum, s)

  return (maxNum // 2) + isOdd