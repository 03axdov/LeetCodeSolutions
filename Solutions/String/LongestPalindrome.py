from calendar import c
from collections import Counter
def longestPalindrome(s: str) -> int:
    count = Counter(s)
    values = sorted(count.values(), key=None, reverse=True)
    currentCount = 0

    for t, value in enumerate(values):
        if value // 2 >= 1:
            values[t] -= 2 * (value // 2)
            currentCount += (value // 2) * 2

    if 1 in values:
        currentCount += 1

    return currentCount

print(longestPalindrome('aaaaAAA'))