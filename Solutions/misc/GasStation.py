def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost): return -1
    
    start = 0
    currentGas = 0
    for i in range(len(gas)):
        currentGas = currentGas + gas[i] - cost[i]
        
        if currentGas < 0:
            start = i + 1
            currentGas = 0
        
    return start