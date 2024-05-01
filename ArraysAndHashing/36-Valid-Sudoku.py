# https://leetcode.com/problems/valid-sudoku/description/
# https://www.youtube.com/watch?v=TjFXEUCMqI8

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# - Only the filled cells need to be validated according to the mentioned rules.

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board) -> bool:
        rows = defaultdict(set) # row map
        cols = defaultdict(set) # col map
        squares = defaultdict(set) # key = (i // 3, j // 3) # square map
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                # Check if the number is already present in the row, column, or square.
                if (board[i][j] in rows[i] or
                    board[i][j] in cols[j] or
                    board[i][j] in squares[(i // 3, j // 3)]):
                    return False

                # Add the number to the row, column, and square maps.
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i // 3, j // 3)].add(board[i][j])
        
        return True
