class Solution(object):
    shortestPaths = []

    def minPathSum(self, grid):
        self.shortestPath = [[0] * len(row) for row in grid]
        startRow = len(grid) - 1
        startCol = len(grid[0]) - 1
        
        return self.traverse(grid, startRow, startCol)
        
        
    def traverse(self, grid, startRow, startCol):
        if startRow == 0 and startCol == 0: return grid[startRow][startCol]
        if startRow < 0 or startCol < 0: return float("inf")

        if self.shortestPath[startRow][startCol] == 0:
            
            self.shortestPath[startRow][startCol] = grid[startRow][startCol] + min(self.traverse(grid, startRow-1, startCol),
                    self.traverse(grid, startRow, startCol-1))
            
        return self.shortestPath[startRow][startCol]
    
    
sol = Solution()
print(sol.minPathSum([[1,2,5],[3,2,1]]))