def isPowerOfFour(n: int) -> bool:
    x = 0
    while 4**x < n:
        x+=1
    
    if 4**x == n:
        return True
    return False