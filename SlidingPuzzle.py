class Solution(object):
    unsolvableBoards = set()

    def toTuple(self, board):
        return tuple(map(tuple, board))

    def shiftZero(self, board, oldCoords, newCoords):
        oldX, oldY = oldCoords
        newX, newY = newCoords
        if newX > 2 or newX < 0 or newY > 1 or newY < 0: return []
        
        tempEl = board[newY][newX]
        board[newY][newX] = 0
        board[oldY][oldX] = tempEl
        return board

    def slidingPuzzleHelper(self, board, moves):
        if len(board) == 0 or self.toTuple(board) in self.unsolvableBoards:
            return -1
        
        if board[0] == [1,2,3] and board[1] == [4,5,0]:
            return moves
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 0:
                    board1 = self.shiftZero(board, [x, y], [x+1, y])
                    board2 = self.shiftZero(board, [x, y], [x-1, y])
                    board3 = self.shiftZero(board, [x, y], [x, y+1])
                    board4 = self.shiftZero(board, [x, y], [x, y-1])
                    
                    positive = []
                    if self.toTuple(board1) not in self.unsolvableBoards:
                        alt1 = self.slidingPuzzleHelper(board1, moves+1)
                        if alt1 >= 0: positive.append(alt1)
                        else: self.unsolvableBoards.add(self.toTuple(board1))
                    if self.toTUple(board2) not in self.unsolvableBoards:
                        alt2 = self.slidingPuzzleHelper(board2, moves+1)
                        if alt2 >= 0: positive.append(alt2)
                        else: self.unsolvableBoards.add(self.toTuple(board2))
                    if self.toTUple(board3) not in self.unsolvableBoards:
                        alt3 = self.slidingPuzzleHelper(board3, moves+1)
                        if alt3 >= 0: positive.append(alt3)
                        else: self.unsolvableBoards.add(self.toTuple(board3))
                    if self.toTUple(board4) not in self.unsolvableBoards:
                        alt4 = self.slidingPuzzleHelper(board4, moves+1)
                        if alt4 >= 0: positive.append(alt4)
                        else: self.unsolvableBoards.add(self.toTuple(board4))
                    
                    if len(positive) == 0:
                        self.unsolvableBoards.add(self.toTuple(board))
                        return -1
                    
                    else: return min(positive)
                        
    def slidingPuzzle(self, board):
        return self.slidingPuzzleHelper(board, 0)

