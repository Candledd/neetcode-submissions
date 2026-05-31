class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            boxRow = row // 3
            for col in range(9):
                num = board[row][col]
                boxCol = col // 3

                if num == ".":
                    continue
                
                if (num in rows[row] or 
                    num in columns[col] or 
                    num in boxes[boxRow, boxCol]):
                    return False
                
                rows[row].add(num)
                columns[col].add(num)
                boxes[boxRow, boxCol].add(num)
        return True       
        