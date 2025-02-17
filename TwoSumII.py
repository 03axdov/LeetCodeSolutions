from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    for i in range(len(numbers)):
        curr = numbers[i]
        
        l = i + 1
        r = len(numbers) - 1
        while l <= r:
            j = (l + r) // 2
            if numbers[j] == target - curr: return [i+1, j+1]
            elif numbers[j] < target - curr:
                l = j + 1
            else:
                r = j - 1
    
    return [-1, -1]