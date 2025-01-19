from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
    res = 0
    prevDigit = 1
    for digit in C:
        res += min(abs(digit - prevDigit), N - abs(digit - prevDigit))
        prevDigit = digit
        
    return res


N = 10
M = 4
C = [9, 4, 4, 8]

print(getMinCodeEntryTime(N, M, C))