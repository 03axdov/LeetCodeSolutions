def maxProfit(prices):
    output = 0
    currentMax = 0
    currentMin = float("inf")

    for i in prices:
        if i < currentMin:
            currentMin = i
            currentMax = 0
        elif i >= currentMax:
            currentMax = i
            if currentMax - currentMin > output:
                output = currentMax - currentMin
    
    return output


print(maxProfit([3,3,5,0,0,3,1,4]))