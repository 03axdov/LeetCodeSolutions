def maxProfit(self, prices):
    currentRes = 0
    currentMin = float("inf")
    
    for price in prices:
        if price < currentMin: currentMin = price
        else:
            currentRes = max(currentRes, price - currentMin)
            
    return currentRes