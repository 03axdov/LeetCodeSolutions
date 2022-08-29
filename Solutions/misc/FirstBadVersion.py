def isBadVersion(version):
    pass

def firstBadVersion(n: int) -> int:
    l, r = 0, n

    while l <= r:
        center = (r+l) // 2
        if isBadVersion(center):
            r = center
        else:
            l = center + 1
            if isBadVersion(center + 1):
                return center + 1