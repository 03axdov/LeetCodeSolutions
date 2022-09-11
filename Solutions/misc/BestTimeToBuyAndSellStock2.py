def maxProfit(prices) -> int:
    currentStock = float("inf")

    for i in range(len(prices)):
        if prices(i) < currentStock:
            pass