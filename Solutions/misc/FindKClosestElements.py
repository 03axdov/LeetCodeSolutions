from typing import List

def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    def key_f(ai):
        return abs(ai - x)

    arr.sort(key=key_f)
    return sorted([arr[i] for i in range(k)])


print(findClosestElements([1,2,3,4,5], 4, 3))