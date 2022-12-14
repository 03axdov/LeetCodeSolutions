def minRefuelStops(target, startFuel, stations):
    dp = [startFuel] + [0] * len(stations)
    for i, (location, capacity) in enumerate(stations):
        for t in range(i, -1, -1):
            if dp[t] >= location:
                dp[t+1] = max(dp[t+1], dp[t] + capacity)

    for i, d in enumerate(dp):
        if d >= target: return i
    return -1
    


print(minRefuelStops(10000000, 100000000, [[5,1000000000],[1000,1000000000],[100000,1000000000]]))