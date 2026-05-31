class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row
        for row in range(9):
            rowSet = set()
            for indx in range(9):
                if board[row][indx] == ".":
                    continue
                if board[row][indx] in rowSet:
                    return False
                rowSet.add(board[row][indx])

        #col
        for col in range(9):
            colSet = set()
            for indx in range(9):
                if board[indx][col] == ".":
                    continue
                if board[indx][col] in colSet:
                    return False
                colSet.add(board[indx][col])

        #square
        for square in range(9):
            squareSet = set()
            for squareRow in range(3):
                for squareCol in range(3):
                    boardRow = (square//3) * 3 + squareRow
                    boardCol = (square%3) * 3 + squareCol
                    if board[boardRow][boardCol] == ".":
                        continue
                    if board[boardRow][boardCol] in squareSet:
                        return False
                    squareSet.add(board[boardRow][boardCol])
        return True

                
            
        
