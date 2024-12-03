def minimumTotal(triangle):
    for row in range(1, len(triangle)):
        for col in range(len(triangle[row])):
            if col == 0:
                triangle[row][col] += triangle[row-1][col]
                continue
            if  col == len(triangle[row]) - 1:
                triangle[row][col] += triangle[row-1][col-1]
                continue
            triangle[row][col] += min(triangle[row-1][col-1], triangle[row-1][col])
        
    return min(triangle[-1])


print(minimumTotal([[-1],[2,3],[1,-1,-3]]))