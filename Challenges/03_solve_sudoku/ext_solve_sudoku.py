### Challenge 03
### Solve Sudoku
### External Solution



### Definition of the solution

# Class for the solution
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        
        # Function to check whether it is safe to insert a number in board or not
        def safe(row,col,k,board):
            for i in range(9):
                # For checking element in same row
                if board[row][i]==k:
                    return False
                # For checking element in same column
                if board[i][col]==k:
                    return False
                # For checking element in same box
                if board[3*(row//3)+i//3][3*(col//3)+i%3]==k:
                    return False
            return True
        
        # Function to solve the board iteratively
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        for k in range(1,10):
                            k=str(k)
                            if safe(i,j,k,board):
                                board[i][j]=k
                                if solve(board):
                                    return True
                                board[i][j]='.'
                        # If it is not possible to insert any particular value at that cell
                        return False 
            # If all the values are filled then it will return True
            return True
        
        # Execution of the solution
        solve(board)
        return board



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
board_2 = [[".",".",".",".",".",".",".",".","."]
,["7",".",".",".","8",".",".",".","5"]
,["2",".",".","9",".",".","3",".","."]
,["9",".",".","7",".",".",".",".","8"]
,["4","7",".","3",".",".",".","5","."]
,[".",".",".","4",".",".",".",".","1"]
,["5",".",".",".","6",".",".",".","2"]
,[".","1","4",".",".",".",".",".","."]
,[".",".","2",".","9",".",".","1","."]]
board_3 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
board_4 = [["2","5",".",".",".",".",".",".","4"]
,[".",".",".",".","5",".",".",".","9"]
,[".","8",".","3",".",".","2","5","."]
,[".",".",".",".",".",".",".",".","2"]
,[".","3",".",".",".","7",".",".","."]
,["8",".",".",".","4",".","1","6","."]
,["1",".",".",".","6",".","5","8","."]
,[".",".",".",".",".",".",".","9","."]
,[".",".","6","4",".",".",".",".","."]]
board_5 = [[".","4",".",".","1","9",".","7","6"]
,["8",".",".",".",".",".",".",".","3"]
,[".",".",".","6",".",".",".",".","."]
,[".","9",".",".","2","7",".","1","."]
,[".",".","4",".",".",".","9",".","."]
,[".",".",".",".",".","5",".",".","."]
,[".",".","3",".","6","2",".",".","7"]
,[".","2",".","5",".",".",".",".","."]
,[".",".",".","4",".",".",".","6","."]]
board_6 = [[".",".","1",".",".","4","8",".","."]
,[".",".","3","2","8",".",".",".","5"]
,[".","2",".",".",".","6",".",".","."]
,[".",".","5",".",".",".",".","7","."]
,[".","3",".","9","1",".","6",".","."]
,[".",".",".",".",".","2",".",".","."]
,[".","9",".","8","3",".","1",".","."]
,["1",".",".",".",".",".",".",".","6"]
,[".",".",".",".","4",".",".",".","."]]
board_7 = [["1",".",".",".","6",".",".",".","."]
,[".",".","3","9",".","1",".","4","."]
,["2",".",".",".",".",".",".",".","7"]
,[".",".",".",".","8",".",".","5","."]
,[".",".","6",".","4",".",".",".","."]
,["3",".",".","5",".","6","2",".","."]
,[".",".","1","3",".","5",".","9","."]
,[".",".",".","8",".",".",".",".","."]
,[".","9",".",".",".",".","4",".","."]]

# Executions
print('--------------------------------------------')
print('Example 1')
ext_result_1 = Solution.solveSudoku(Solution,board_1)
print(ext_result_1)
print('--------------------------------------------')
print('Example 2')
ext_result_2 = Solution.solveSudoku(Solution,board_2)
print(ext_result_2)
print('--------------------------------------------')
print('Example 3')
ext_result_3 = Solution.solveSudoku(Solution,board_3)
print(ext_result_3)
print('--------------------------------------------')
print('Example 4')
ext_result_4 = Solution.solveSudoku(Solution,board_4)
print(ext_result_4)
print('--------------------------------------------')
print('Example 5')
ext_result_5 = Solution.solveSudoku(Solution,board_5)
print(ext_result_5)
print('--------------------------------------------')
print('Example 6')
ext_result_6 = Solution.solveSudoku(Solution,board_6)
print(ext_result_6)
print('--------------------------------------------')
print('Example 7')
ext_result_7 = Solution.solveSudoku(Solution,board_7)
print(ext_result_7)
print('--------------------------------------------')