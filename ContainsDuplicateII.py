def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    dic = {}    # key: num, value: list of indexes ascending
    
    for i in range(len(nums)):
        curr = nums[i]
        if curr in dic.keys():
            for j in list(reversed(dic[curr])):
                if abs(i - j) > k: break
                if nums[i] == nums[j]: return True
            dic[curr].append(i)
        else:
            dic[curr] = [i]
            
    return False