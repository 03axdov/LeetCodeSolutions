from collections import Counter
def reorderedPowerOf2(n: int) -> bool:
    count = Counter(str(n))
    i = 0
    while 2**i <= 10**9 :
        if Counter(str(2**i)) == count: return True
        i += 1
    return False


print(reorderedPowerOf2(10**9))