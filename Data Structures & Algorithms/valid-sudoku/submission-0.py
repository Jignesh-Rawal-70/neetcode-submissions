class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = {}, {}, {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                
                current_items_in_row = rows.get(i, set())
                if board[i][j] not in current_items_in_row:
                    current_items_in_row.add(board[i][j])
                    rows[i] = current_items_in_row
                else:
                    return False
                
                current_items_in_col = cols.get(j, set())
                if board[i][j] not in current_items_in_col:
                    current_items_in_col.add(board[i][j])
                    cols[j] = current_items_in_col
                else:
                    return False

                square_key = (i // 3, j // 3)
                current_items_in_square = squares.get(square_key, set())
                if board[i][j] not in current_items_in_square:
                    current_items_in_square.add(board[i][j])
                    squares[square_key] = current_items_in_square
                else:
                    return False
        
        return True