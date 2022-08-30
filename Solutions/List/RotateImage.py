def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(f"Matrix: {matrix}")
        

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rotate(matrix)

print(matrix)

