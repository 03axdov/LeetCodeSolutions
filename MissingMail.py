from typing import List


dic = {}
def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    global dic
    dic = {}
    res = getMaxExpectedProfitHelper(N, V, C, S, 0)
    return res


def getMaxExpectedProfitHelper(N: int, V: List[int], C: int, S: float, mailRoom, startI=0) -> float:
    global dic
    alts = []
    cash = 0
    
    for i in range(N):
        mailRoom += V[i]
        
        if i + startI not in dic.keys():
            print(i + startI)
            dic[i + startI] = getMaxExpectedProfitHelper(N - i - 1, V[i+1:], C, S, mailRoom * (1 - S), i + startI+1)  # If we don't take
            
        alts.append(cash + dic[i + startI])
        
        cash += mailRoom - C
        mailRoom = 0
    
    print(alts)    

    dic[startI] = max([cash, max(alts, default=0)])
    return dic[startI]

N = 5
V = [10, 2, 8, 6, 4]
C = 3
S = 0.15
print(getMaxExpectedProfit(N, V, C, S))