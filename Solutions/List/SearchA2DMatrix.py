def searchMatrix(matrix, target):
    for i in range(len(matrix)):
        if i != 0:
            if matrix[i][0] > target and matrix[i-1][0] <= target:
                for j in matrix[i-1]:
                    if j == target:
                        return True
                    if j > target:
                        return False
                return False
        if i == len(matrix) - 1:
            for j in matrix[i]:
                if j == target:
                    return True
                if j > target:
                    return False
            return False
    return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 23))