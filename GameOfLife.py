def gameOfLife(self, board: List[List[int]]) -> None:
    numberNeighbors = {}
    for row in range(len(board)):
        for col in range(len(board[0])):
            neighbors = 0
            
            if row > 0:
                neighbors += sum(board[row - 1][max(0, col-1): min(len(board[0]) - 1, col+1)+1])
            if row < len(board) - 1:
                neighbors += sum(board[row + 1][max(0, col-1): min(len(board[0]) - 1, col+1)+1])
            if col > 0: neighbors += board[row][col-1]
            if col < len(board[0]) - 1: neighbors += board[row][col+1]
            
            numberNeighbors[(row, col)] = neighbors
            
    for row in range(len(board)):
        for col in range(len(board[0])):
            neighbors = numberNeighbors[(row, col)]
            val = board[row][col]
            if neighbors < 2 and val == 1: board[row][col] = 0
            elif neighbors > 3 and val == 1: board[row][col] = 0
            elif neighbors == 3 and val == 0: board[row][col] = 1