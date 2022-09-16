from heapq import *
def maxPerformance(n: int, speed, efficiency, k: int) -> int:
    cur_sum, h = 0, []
    ans = -float('inf')
    
    for i, j in sorted(zip(efficiency, speed),reverse=True):
        while len(h) > k-1:
            cur_sum -= heappop(h)
        heappush(h, j)
        cur_sum += j
        ans = max(ans, cur_sum * i)
        
    return ans % (10**9+7)

print(maxPerformance(6, [2,10,5,3,1,5,8], [5,4,4,3,9,7,2], 2))