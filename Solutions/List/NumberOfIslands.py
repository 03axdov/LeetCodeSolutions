class Solution(object):
    discoveredIslandTiles = set()

    def traverseIsland(self, grid, row, col):
        if row >= len(grid) or col >= len(grid[0]): return
        if row < 0 or col < 0: return
        if (row, col) in discoveredIslandTiles: return
        
        tile = grid[row][col]
        if tile == "1":
            self.discoveredIslandTiles.add((row, col))

            self.traverseIsland(grid, row-1, col)
            self.traverseIsland(grid, row+1, col)
            self.traverseIsland(grid, row, col-1)
            self.traverseIsland(grid, row, col+1)
        else:
            return


    def numIslands(self, grid):
        self.discoveredIslandTiles = set()
        
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                tile = grid[row][col]
                if tile == "1" and (row, col) not in self.discoveredIslandTiles:
                    res += 1
                    self.traverseIsland(grid, row, col)
                    
        return res