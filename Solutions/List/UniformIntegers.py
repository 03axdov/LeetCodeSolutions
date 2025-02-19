def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    res = 0
    currentLen = len(str(A))
    i = int("1" * currentLen)
    
    
    while i <= B:
        if i >= A: res += 1
        
        if len(str(i)) > currentLen:
            currentLen += 1
            i = int("1" * currentLen)
            
        i += int("1" * currentLen)
    
    return res


print(getUniformIntegerCountInInterval(1, 9))