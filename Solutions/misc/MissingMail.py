from typing import List
# Write any import statements here


def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    mailRoom = 0
    cash = 0
    
    for i in range(N):
        mailRoom += V[i]
        
        countUnworth = 1
        for j in range(i+1,N):
            if C >= S * V[j]:
                countUnworth += 1
            else:
                break
    
        if C < S * countUnworth * mailRoom or (i == N - 1 and C < mailRoom):
            print(f"i: {i}, countUnworth: {countUnworth}")
            cash += mailRoom - C
            mailRoom = 0
            
        mailRoom = mailRoom * (1 - S)
    
    return cash


N = 5
V = [10, 2, 8, 6, 4]
C = 3
S = 0.15
print(getMaxExpectedProfit(N,V,C,S))