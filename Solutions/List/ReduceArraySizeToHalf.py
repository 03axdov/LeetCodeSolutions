from collections import Counter
def minSetSize(arr):
    count = Counter(arr)
    currentCount = 0
    currentSize = 0
    for value in sorted(count.values(), key=None, reverse=True):
        currentSize += 1
        if currentCount + value >= len(arr) // 2:
            return currentSize
        currentCount += value


print(minSetSize([3,3,3,3,5,5,5,2,2,7]))
