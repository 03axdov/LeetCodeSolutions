def convert(s: str, numRows: int) -> str:
    rows = [''] * numRows
    direction = 1
    current = 0
    if numRows == 1: return s

    for char in s:
        rows[current] += char
        if current == 0: direction = 1
        if current == numRows - 1: direction = -1

        current += direction

    output = ''
    for row in rows:
        output += row
    
    return output

print(convert('', 3))