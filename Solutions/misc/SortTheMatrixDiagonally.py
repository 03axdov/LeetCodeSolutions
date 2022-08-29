def diagonalSort(mat):
    output = [[0] * len(row) for row in mat]
    for i in range(len(mat[0])):
        current = 0
        start = i
        current_diagonal = []
        while True:
            try:
                current_diagonal.append(mat[current][start])
                current += 1
                start += 1
            except IndexError:
                current_diagonal = sorted(current_diagonal)
                current = 0
                start = i
                for num in current_diagonal:
                    output[current][start] = num
                    current += 1
                    start += 1

                break
    
    for i in range(1, len(mat)):
        current = 0
        start = i
        current_diagonal = []
        while True:
            try:
                current_diagonal.append(mat[start][current])
                current += 1
                start += 1
            except IndexError:
                current_diagonal = sorted(current_diagonal)
                current = 0
                start = i
                for num in current_diagonal:
                    output[start][current] = num
                    current += 1
                    start += 1

                break


    return output


print(diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))