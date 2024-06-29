from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or board[r][c] == "X":
                return
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        #1. Capture all the Unsurrounded Regions first using DFS
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS - 1] or c in [0, COLS - 1]) and board[r][c] == "O":
                    dfs(r, c)
        
        #2. Capture all the Surrounded Regions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        #2. Revert all the Unsurrounded Regions T -> 0       
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        

#Test Cases
mySolution = Solution()
testcase1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
testcase2 = [["X"]]
mySolution.solve(testcase1)
mySolution.solve(testcase2)
print("Test Case 1", testcase1)
print("Test Case 2", testcase2)
                
