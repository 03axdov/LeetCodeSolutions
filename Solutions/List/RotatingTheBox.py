def rotateTheBox(box):
    m = len(box)
    n = len(box[0])
    
    # Rotate the box
    
    rotated = [[[] for _ in range(m)] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            rotated[j][i] = box[m - i - 1][j]
            
    # Dropdown
    for i in range(1, n+1):
        for j in range(m):
            current = rotated[n - i][m - j - 1]
            print(current)
            if (current != "#"): continue

            for offset in range(n - i + 1, n):
                belowC = rotated[offset][m - j - 1]
                if belowC != ".": break # Reached an obstacle
                rotated[offset - 1][m - j - 1] = "."
                rotated[offset][m - j - 1] = "#"
                
    return rotated
    
    
box = [["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]
print(rotateTheBox(box))