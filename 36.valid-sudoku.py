#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # checking rows
        for i in range(9):
            row_board = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_board:
                        print(board[i][j])
                        print("A")
                        return False
                    row_board.add(board[i][j])

        # checking columns
        for i in range(9):
            column_board = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in column_board:
                        print(board[j][i])
                        print("B")
                        return False
                    column_board.add(board[j][i])
        
        # checking per 3x3 row column

        for right in [0, 3, 6]:
            for down in [0, 3, 6]:
                board_set = set()
                for i in range(3):
                    for j in range(3):
                        curr_i, curr_j = i+down, j+right
                        if board[curr_i][curr_j] != ".":
                            if board[curr_i][curr_j] in board_set:
                                print(board[curr_i][curr_j])
                                print("C")
                                return False
                            board_set.add(board[curr_i][curr_j])
        
        return True

        
# @lc code=end

