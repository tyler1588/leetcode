class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                if board[i][j].isdigit():
                    s.add(board[i][j])
        
        # check cols
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                if board[j][i].isdigit():
                    s.add(board[j][i])
        
        # check squares
        vals = [0, 3, 6]
        checks = [0, 1, 2]
        for i in vals:
            for j in vals:
                s = set()
                for k in checks:
                    for l in checks:
                        if board[i+k][j+l] in s:
                            return False
                        if board[i+k][j+l].isdigit():
                            s.add(board[i+k][j+l])
        
        # valid board
        return True