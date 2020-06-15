class Solution(object):
    def isValidSudoku(self, board):
        for rol in range(9):
            rol_set = set()
            col_set = set()
            for col in range(9):
                if board[rol][col] != '.':
                    if board[rol][col] in rol_set or board[rol][col]<'1' or board[rol][col]>'9':
                        return False
                    rol_set.add(board[rol][col])
                if board[col][rol] != '.':
                    if board[col][rol] in col_set or board[col][rol]<'1' or board[col][rol]>'9':
                        return False
                    col_set.add(board[col][rol])
        for begin_rol in range(0, 9, 3):
            for begin_col in range(0, 9, 3):
                rect_set = set()
                for rol in range(3):
                    for col in range(3):
                        if board[begin_rol+rol][begin_col+col] != '.':
                            if board[begin_rol+rol][begin_col+col] in rect_set or board[begin_rol+rol][begin_col+col]<'1' or board[begin_rol+rol][begin_col+col]>'9':
                                return False
                            rect_set.add(board[begin_rol+rol][begin_col+col])
        return True


if __name__ == '__main__':
    li = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(li))