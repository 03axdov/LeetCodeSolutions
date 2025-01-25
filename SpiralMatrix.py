from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    lRow = 0
    rRow = len(matrix) - 1
    lCol = 0
    rCol = len(matrix[0]) - 1
    
    endSize = len(matrix) * len(matrix[0])
    res = []
    while lRow <= rRow or lCol <= rCol:
        
        for c in range(lCol, rCol + 1):
            res.append(matrix[lRow][c])
        if len(res) == endSize: break
        lRow += 1
        for r in range(lRow, rRow + 1):
            res.append(matrix[r][rCol])
        if len(res) == endSize: break
        rCol -= 1
        for c in range(rCol, lCol-1, -1):
            res.append(matrix[rRow][c])
        if len(res) == endSize: break
        rRow -= 1
        for r in range(rRow, lRow-1, -1):
            res.append(matrix[r][lCol])
        if len(res) == endSize: break
        lCol += 1
    
    return res


print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))