def numIslands(grid):
    h, w = len(grid), len(grid[0])
    current = 0

    def dfs(i, j):
        grid[i][j] = -1 # Visited
        for i2, j2 in (1, 0), (-1, 0), (0, 1), (0, -1):
            ii, jj = i + i2, j + j2
            if h > ii >= 0 and 0 <= jj < w and grid[ii][jj] == '1':
                dfs(ii, jj)
    
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '1':
                current += 1
                dfs(i, j)

    return current


print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))