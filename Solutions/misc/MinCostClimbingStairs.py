def minCostClimbingStairs(cost):
    if not cost: return
    min_cost = [0] * len(cost)

    for i in range(len(cost)):
        if i == 0:
            min_cost[0] = cost[0]
        elif i == 1:
            min_cost[1] = cost[1]
        else:
            min_cost[i] = min(min_cost[i-1], min_cost[i-2]) + cost[i]

    return min(min_cost[-1], min_cost[-2])



print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))