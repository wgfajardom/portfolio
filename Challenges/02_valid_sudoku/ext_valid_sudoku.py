### Challenge 02
### Valid Sudoku
### External Solution


### Definition of the solution

# Import libraries
import collections

# Class for the solution
class Solution:
    def IsValidSudoku(self, board) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True     


### Testing External Solution

# Initialize inputs
board_1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
board_2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
board_3 = [["5","4","3"]
,["2",".","."]
,[".","9","."]]

# Executions
print('--------------------------------------------')
print('Example 1')
ext_result_1 = Solution.IsValidSudoku(Solution, board_1)
print(ext_result_1)
print('--------------------------------------------')
print('Example 2')
ext_result_2 = Solution.IsValidSudoku(Solution, board_2)
print(ext_result_2)
print('--------------------------------------------')
print('Example 3')
try: 
    ext_result_3 = Solution.IsValidSudoku(Solution, board_3)
except:
    ext_result_3 = "The board is not valid"
print(ext_result_3)
print('--------------------------------------------')
