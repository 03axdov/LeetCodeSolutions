def floodFill(image, sr, sc, color):
    originalColor = float('inf')
    if image[sr][sc] == color: return image
    flood(image, sr, sc, color, originalColor)
    return image

def flood(image, sr, sc, color, originalColor):
    if originalColor == float('inf'): originalColor = image[sr][sc]
    if 0 > sr or sr >= len(image) or 0 > sc or len(image[0]) <= sc or image[sr][sc] != originalColor: return
    image[sr][sc] = color
    for (i, j) in [(1,0), (0,1), (-1, 0), (0, -1)]: flood(image, sr+i, sc+j, color, originalColor)


print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))