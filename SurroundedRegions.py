seenRegions = set()
currentRegion = set()
currentRegionIsSurrounded = True

def solve(self, board):
    self.seenRegions = set()
    self.currentRegion = set()
    self.currentRegionIsSurrounded = True
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "X": continue
            if (row, col) in self.seenRegions: continue
            self.traverse(board, row, col)
            
            for r, c in self.currentRegion:
                if self.currentRegionIsSurrounded:
                    board[r][c] = "X"

                seenRegions.add((r, c))
                
            self.currentRegion = set()
            self.currentRegionIsSurrounded = True
            


def traverse(self, board, row, col):
    if row < 0 or row >= len(board): return
    if col < 0 or col >= len(board[0]): return
    
    if board[row][col] == "X": return   
    if (row, col) in self.currentRegion or (row, col) in self.seenRegions: return

    if row == 0 or row == len(board) - 1: self.currentRegionIsSurrounded = False
    if col == 0 or col == len(board[0]) - 1: self.currentRegionIsSurrounded = False
    
    self.currentRegion.add((row, col))
    
    self.traverse(board, row-1, col)
    self.traverse(board, row+1, col)
    self.traverse(board, row, col+1)
    self.traverse(board, row, col-1)
    
    
"""
["X","O","O","X","X","X","O","X","O","O"]
["X","O","X","X","X","X","X","X","X","X"]
["X","X","X","X","O","X","X","X","X","X"]
["X","O","X","X","X","O","X","X","X","O"]
["O","X","X","X","O","X","O","X","O","X"]
["X","X","O","X","X","O","O","X","X","X"]
["O","X","X","O","O","X","O","X","X","O"]
["O","X","X","X","X","X","O","X","X","X"]
["X","O","O","X","X","O","X","X","O","O"]
["X","X","X","O","O","X","O","X","X","O"]
"""