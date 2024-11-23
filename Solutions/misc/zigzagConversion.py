def convert(s: str, numRows: int) -> str:
    if numRows == 1: return s

    rows = [""] * numRows
    currentRow = 0
    directionUp = True
    for char in s:
        rows[currentRow] += char
        if currentRow == numRows - 1 or currentRow == 0:
            directionUp = not directionUp
        
        if directionUp:
            currentRow -= 1
        else:
            currentRow += 1

    result = ""
    for row in rows:
        result += row
        
    return result