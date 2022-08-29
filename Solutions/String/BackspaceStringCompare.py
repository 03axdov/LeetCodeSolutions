def backspaceCompare(s, t):
    idxS, idxT = 0, 0
    currentS, currentT = '', ''
    while idxS <= len(s) - 1 or idxT <= len(t) - 1:
        if idxS != len(s):
            if s[idxS] != '#':
                currentS += s[idxS]
            else:
                currentS = currentS[0:-1]
            idxS += 1
        if idxT != len(t):
            if t[idxT] != '#':
                currentT += t[idxT]
            else:
                currentT = currentT[0:-1]
            idxT += 1
        
    return currentS == currentT


print(backspaceCompare("ab#c", "adc"))