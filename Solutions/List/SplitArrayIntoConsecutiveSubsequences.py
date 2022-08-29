from collections import Counter, defaultdict
def isPossible(nums):
    counts = Counter(nums)
    dic = defaultdict(int)

    for num in nums:
        if not counts[num]: continue

        if dic[num-1] > 0:
            dic[num-1] -= 1
            dic[num] += 1
            counts[num] -= 1

        else:
            if not counts[num+1] or not counts[num+2]:
                return False
            counts[num] -= 1
            counts[num+1] -= 1
            counts[num+2] -= 1
            dic[num+2] += 1
    
    return True

            
            


print(isPossible([1,2,3,3,4,5]))