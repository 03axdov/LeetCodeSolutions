from collections import Counter
def firstUniqChar(s):
    counter = Counter(s)
    for count in counter:
        if counter[count] == 1:
            return s.index(count)
    return -1


print(firstUniqChar("dddccdbba"))