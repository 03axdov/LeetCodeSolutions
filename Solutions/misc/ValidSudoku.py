def isValidSudoku(self, board: List[List[str]]) -> bool:
    
    subBoxes = {} # Key: "{row // 3}-{col // 3}", value: set of digits
    rows = {} # Key: row idx, value: set of digits
    cols = {} # Key: col idx, value: set of digits
    
    for row in range(len(board)):
        if row not in rows.keys(): rows[row] = set([])
        
        for col in range(len(board[row])):
            if col not in cols.keys(): cols[col] = set([])
            
            val = board[row][col]
            if val == ".": continue
            
            if val in rows[row] or val in cols[col] or int(val) > 9 or int(val) < 0: return False
            
            subBox = f"{row // 3}-{col // 3}"
            if subBox not in subBoxes.keys(): subBoxes[subBox] = set([])
            if val in subBoxes[subBox]: return False
            
            rows[row].add(val)
            cols[col].add(val)
            subBoxes[subBox].add(val)
            
    return True