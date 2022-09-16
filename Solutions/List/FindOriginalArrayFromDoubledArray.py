from collections import defaultdict
def findOriginalArray(changed):
    length = len(changed)
    doubles = defaultdict(int)
    original = []

    if length % 2 != 0: return

    changed = sorted(changed)
    for i in changed:
        if doubles[i] != 0:
            doubles[i] -= 1
            original.append(i // 2)
        else:
            doubles[i*2] += 1

    if len(original) != length // 2: return
    return original


print(findOriginalArray([6,3,0,1]))