def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    res = 0
    
    for i in range(2):
        numPhotographers = 0
        for c in C[X:Y]:
            if c == "P": numPhotographers += 1
        numBackgrounds = 0
        for c in C[Y+X:2*Y]:
            if c == "B": numBackgrounds += 1
        
        for t, c in enumerate(C[Y:]):
            if t + 2*Y < len(C) and C[t + 2*Y] == "B": numBackgrounds += 1
            
            if c == ".": continue
            
            if c == "A":
                res += numPhotographers * numBackgrounds
            if C[Y+t-X] == "P": numPhotographers += 1
            if c == "B": numBackgrounds -= 1
                
            if C[t] == "P": numPhotographers -= 1
            
        C = list(reversed(C))
        
        
    return res


N = 8
C = ".PBAAP.B"
X = 1
Y = 3
print(getArtisticPhotographCount(N,C,X,Y))