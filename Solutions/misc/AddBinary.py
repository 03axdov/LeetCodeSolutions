def addBinary(a, b):
    aI = len(a) - 1
    bI = len(b) - 1
    carry = 0
    res = ""
    
    while aI >= 0 or bI >= 0 or carry > 0:
        if aI >= 0:
            carry += int(a[aI])
            aI -= 1
        if bI >= 0:
            carry += int(b[bI])
            bI -= 1
            
        res = str(carry % 2) + res
        carry = carry // 2
    
    return res


print(addBinary("11", "1"))