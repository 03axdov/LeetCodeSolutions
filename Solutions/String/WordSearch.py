def exist(self, board: List[List[str]], word: str) -> bool:
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == word: return True
            res = self.find_word(board, word, row, col, set([]))
            if res: return True
            
    return False
        
        
def find_word(self, board, word, row, col, seen):
    if not word: return True
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]): return False
    if board[row][col] != word[0]: return False
    if (row, col) in seen: return False
    
    seen.add((row, col))
    
    return (
        self.find_word(board, word[1:], row-1,col,seen.copy()) or
        self.find_word(board, word[1:], row+1,col,seen.copy()) or
        self.find_word(board, word[1:], row,col-1,seen.copy()) or
        self.find_word(board, word[1:], row,col+1,seen.copy())
    )
    