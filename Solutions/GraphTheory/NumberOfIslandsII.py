def numIslands(grid):
    output = 0

    def dfs(grid, i, j):
        if grid[i][j] == "1":
            grid[i][j] = "-1"   # visited
            for ii, jj in (1, 0), (0,1), (-1,0), (0, -1):
                i, j = i + ii, j + jj
                dfs(grid, i, j)
        else:
            return

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                output += 1
                dfs(grid, i, j)

    return output


print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))