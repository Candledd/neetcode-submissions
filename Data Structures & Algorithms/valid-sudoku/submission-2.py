class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            box_row_band = (i // 3) * 3 
            
            for j in range(9):
                num_str = board[i][j]
                
                if num_str == ".":
                    continue
                
                num = int(num_str) - 1
                
                box_idx = box_row_band + (j // 3)
                
                if rows[i][num] or cols[j][num] or boxes[box_idx][num]:
                    return False
                
                rows[i][num] = True
                cols[j][num] = True
                boxes[box_idx][num] = True
                
        return True