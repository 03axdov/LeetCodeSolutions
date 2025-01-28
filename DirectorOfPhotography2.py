def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    res = 0
    
    for i in range(len(C)):
        current = C[i]
        
        if current == "A":
            leftWindow = C[max(0, i-Y):max(i-X+1,0)]
            rightWindow = C[min(i+X, len(C)):min(i+Y+1,len(C))]
            
            numPhotographers = 0
            numBackgrounds = 0
            for el in leftWindow:
                if el == "P": numPhotographers += 1
            for el in rightWindow:
                if el == "B": numBackgrounds += 1
                
            res += numPhotographers*numBackgrounds
           
    C = list(reversed(C)) 
    for i in range(len(C)):
        current = C[i]
        
        if current == "A":
            leftWindow = C[max(0, i-Y):max(i-X+1,0)]
            rightWindow = C[min(i+X, len(C)):min(i+Y+1,len(C))]
            
            numPhotographers = 0
            numBackgrounds = 0
            for el in leftWindow:
                if el == "P": numPhotographers += 1
            for el in rightWindow:
                if el == "B": numBackgrounds += 1
                
            res += numPhotographers*numBackgrounds
    
    return res


N = 5
C = "APABA"
X = 2
Y = 3
print(getArtisticPhotographCount(N,C,X,Y))