
def maxMatrixSum(matrix):
    n = len(matrix)
    smallestAbs = float("inf")
    smallestAbsCoords = [-1,-1]
    
    numNegative = 0

    for i1 in range(n):
        for i2 in range(n):
            if matrix[i1][i2] < 0:
                numNegative += 1
            if abs(matrix[i1][i2]) < smallestAbs:
                smallestAbs = abs(matrix[i1][i2])
                smallestAbsCoords = [i1, i2]
    
    res = 0
    for i1 in range(n):
        for i2 in range(n):
            if i1 != smallestAbsCoords[0] or i2 != smallestAbsCoords[1] or numNegative % 2 == 0:
                res += abs(matrix[i1][i2])
            else:
                res -= abs(matrix[i1][i2])
                
    return res


print(maxMatrixSum([[-1,0,-1],[-2,1,3],[3,2,2]]))